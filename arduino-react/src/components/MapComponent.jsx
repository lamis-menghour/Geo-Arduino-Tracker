import React, { useEffect } from "react";
import { Group, Text, Button } from "@mantine/core";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";

mapboxgl.accessToken =
  "pk.eyJ1IjoibGFtaXMtbWVuZ2hvdSIsImEiOiJjbHBrNjM3cDQwNXU3MmptcjBiaDNlOHR2In0.1LZRmyTKe-ZmfN09xmeE1A";

const MapComponent = ({ data, fetchData }) => {
  const { longitude, latitude } = data;

  useEffect(() => {
    initializeMap(longitude, latitude);
  }, [fetchData]);

  const initializeMap = (longitude, latitude) => {
    const map = new mapboxgl.Map({
      container: "map-container",
      style: "mapbox://styles/mapbox/navigation-day-v1",
      center: [longitude, latitude],
      zoom: 17,
    });

    const nav = new mapboxgl.NavigationControl();
    map.addControl(nav, "top-left");

    new mapboxgl.Marker().setLngLat([longitude, latitude]).addTo(map);
  };

  return (
    <div
      style={{
        margin: 0,
        padding: 0,
        width: "100vw",
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "flex-end",
        alignItems: "center",
        position: "relative",
      }}
    >
      <div
        id="map-container"
        style={{
          width: "100%",
          height: "100%",
          position: "absolute",
          top: 0,
          left: 0,
        }}
      />

      <Group
        justify="center"
        style={{
          background: "rgba(0, 0, 0, 0.2)",
          padding: "10px",
          borderRadius: "5px",
          marginBottom: "20px",
          zIndex: 2,
        }}
      >
        <Text fw={500} size="lg">
          Longitude: {longitude}
        </Text>
        <Text fw={500} size="lg" >
          Latitude: {latitude}
        </Text>
        <Button onClick={fetchData} color="orange" size="md" radius="md">
          Update Location
        </Button>
      </Group>
    </div>
  );
};

export default MapComponent;
