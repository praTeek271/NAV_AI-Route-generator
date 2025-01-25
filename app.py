import folium
from folium.plugins import HeatMap
import requests
from flask import Flask, render_template, request
from folium import PolyLine
import openrouteservice
import herepy


app = Flask(__name__, template_folder='template')


def format_duration(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"


@app.route('/', methods=['POST', 'GET'])
def get_map():
    map_html = None
    formatted_duration = ""
    if request.method == 'POST':
        # Input data
        lat1 = float(request.form['lat1'])
        lng1 = float(request.form['lng1'])
        lat2 = float(request.form['lat2'])
        lng2 = float(request.form['lng2'])
        vehicle_type = request.form['vehicle_type']

        # Ensure valid bounding box
        lat1, lat2 = min(lat1, lat2), max(lat1, lat2)
        lng1, lng2 = min(lng1, lng2), max(lng1, lng2)

        

        # Traffic API request
                                                                                                                                    # HERE API Key
        traffic_url = f"https://data.traffic.hereapi.com/v7/flow?locationReferencing=shape&in=bbox:{lng1},{lat1},{lng2},{lat2}&apiKey={HERE_API_KEY}"
        traffic_response = requests.get(traffic_url)
        traffic_data = traffic_response.json()

        # Handle API errors
        if 'results' not in traffic_data:
            error_message = traffic_data.get('cause', 'Unknown error')
            return render_template('index.html', error=f"Traffic API error: {error_message}")

        # Process traffic data to extract coordinates and traffic intensities
        coordinates = []
        intensities = []  # Collect traffic intensity for heatmap weighting
        for result in traffic_data['results']:
            for link in result['location']['shape']['links']:
                intensity = link.get('trafficDensity', 1)  # Example field, adjust based on API docs
                for point in link['points']:
                    coordinates.append((point['lat'], point['lng']))
                    intensities.append(intensity)

        # Normalize intensity for heatmap weights
        max_intensity = max(intensities) if intensities else 1
        heatmap_data = [(lat, lng, intensity / max_intensity) for (lat, lng), intensity in zip(coordinates, intensities)]

        # Create a map centered at the average of the input coordinates
        m = folium.Map(location=[(lat1 + lat2) / 2, (lng1 + lng2) / 2], zoom_start=14)

        # Add the heatmap layer
        HeatMap(heatmap_data).add_to(m)

        # OpenRouteService API Key
        
        client = openrouteservice.Client(key=openroute_API_KEY) # Initialize client
        coords = [[lng1, lat1], [lng2, lat2]]

        # Set the profile based on the vehicle type
        profile = 'driving-car' if vehicle_type == 'car' else ('cycling-regular' if vehicle_type == 'bicycle' else 'foot-walking')

        # Find the shortest path using OpenRouteService
        route = client.directions(coordinates=coords, profile=profile, format='geojson')

        # Add traffic-based route adjustment logic (optional)
        # Example: Prioritize avoiding high-intensity traffic areas
        # NOTE: Implement based on OpenRouteService API capabilities

        duration = route['features'][0]['properties']['segments'][0]['duration']  # Get duration in seconds

        # Add the route to the map
        folium.GeoJson(route, name='Shortest Path').add_to(m)

        # Add start and end markers to the map
        folium.Marker([lat1, lng1], popup='Start', icon=folium.Icon(color='green', icon='play')).add_to(m)
        folium.Marker([lat2, lng2], popup='End', icon=folium.Icon(color='red', icon='stop')).add_to(m)

        map_html = m._repr_html_()
        formatted_duration = format_duration(duration)

    return render_template('index.html', map_html=map_html, duration=formatted_duration)


if __name__ == '__main__':
    app.run(debug=True)


