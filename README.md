# NAV_AI-Route-generator

![Demo](https://github.com/praTeek271/NAV_AI-Route-generator/blob/master/demo.png)
---
![Demo](https://github.com/praTeek271/NAV_AI-Route-generator/output.gif)

This is a Python web application that allows users to visualize traffic congestion using a heatmap and find the shortest route between two points. It uses the HERE Traffic API for traffic data and the OpenRouteService API for routing information. The application is built using Flask for the web framework and Folium for map visualization.

## Features
Traffic Heatmap: Users can input coordinates (latitude and longitude) for a specific area and view a traffic heatmap that visualizes traffic congestion in that area.

Shortest Route: Users can input the starting and ending coordinates, select a vehicle type (car, bicycle, or foot), and find the shortest route between the two points on the map.

## Prerequisites
Before running the application, make sure you have the following:

Python 3.x installed on your system.

Required Python packages installed. You can install them using pip:



```
pip install folium flask requests openrouteservice herepy
```

## Getting Started

## Steps to Use the Project

To use the NAV_AI-Route-generator project, follow these steps:

1. Clone the GitHub project by running the following command in your terminal:
   ```bash
   git clone https://github.com/praTeek271/NAV_AI-Route-generator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd NAV_AI-Route-generator
   ```

3. Install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the project by running the following command:
   ```bash
   python app.py
   ```

Open your web browser and go to http://localhost:5000 to access the application.

#### ``Now the project is up and running, ready to provide route predictions and traffic management capabilities based on the data and algorithms employed.``

---
***Note:*** *Before running the application, make sure you have the following:*

- *Python 3.x installed on your system.*
---
### Traffic Heatmap:

Enter the latitude and longitude coordinates for a specific area in the input form.
Click the "Show Traffic Heatmap" button to view the traffic congestion heatmap for the selected area.
Shortest Route:

Enter the starting and ending coordinates, select a vehicle type (car, bicycle, or foot) from the dropdown menu.
Click the "Find Shortest Route" button to display the shortest route on the map, along with the estimated duration in hours, minutes, and seconds.
License
This project is licensed under the MIT License. See the LICENSE file for details.
## About the Project

The NAV_AI-Route-generator project aims to provide route prediction and traffic management capabilities using Python. It leverages various data sources, including historical traffic data, real-time traffic updates, and sensor data, to generate accurate predictions and optimize route recommendations.

The project's workflow involves several key steps:

1. **Data Gathering**: Relevant data is collected from multiple sources, such as traffic sensors, GPS devices, and historical traffic databases. This data provides valuable insights into traffic flow, congestion, road conditions, and other factors influencing route selection.

2. **Machine Learning Analysis**: Machine learning algorithms, such as deep learning models like LSTMs or graph convolutional networks (GCNs), are employed to analyze the collected data and generate predictions. These models learn patterns and relationships from historical data to predict future traffic conditions and route outcomes.

3. **Real-Time Updates Integration**: The predictions are combined with real-time traffic updates to further refine and adjust the recommended routes. This ensures that the system adapts to changing traffic conditions and provides the most accurate and up-to-date information to users.

4. **Visualization and User Interaction**: Interactive maps and data visualizations are utilized to visualize the results. Users can view predicted routes, traffic congestion levels, alternative routes, and estimated travel times. Real-time notifications or alerts about significant traffic incidents or changes may also be provided.


---
***Note:*** *The NAV_AI-Route-generator project is designed to be flexible and extensible, allowing for the integration of additional data sources, machine learning models, and visualization tools to enhance its capabilities.*

** ***``
Feel free to explore the project and leverage its features for optimizing your route planning and traffic management needs.
``*** **
