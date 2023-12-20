import React, { useEffect } from "react";
import mapboxgl from "mapbox-gl";

// Replace 'YOUR_MAPBOX_ACCESS_TOKEN' with your actual Mapbox access token
mapboxgl.accessToken =
  "pk.eyJ1IjoibGFtaXMtbWVuZ2hvdSIsImEiOiJjbHBrNjM3cDQwNXU3MmptcjBiaDNlOHR2In0.1LZRmyTKe-ZmfN09xmeE1A";

const MapboxMap = () => {
  // const MapboxMap = ({latitude ,Longitude}) => {
  useEffect(() => {
    // Initialize map when component mounts
    const map = new mapboxgl.Map({
      container: "map-container", // HTML container ID
      style: "mapbox://styles/mapbox/streets-v12", // Map style URL
      center: [5.744284, 36.80022], // Starting position [lng, lat]
      // center: [Longitude, latitude], //
      zoom: 18, // Starting zoom level
    });

    // Clean up the map when the component unmounts
    return () => map.remove();
  }, []); // Empty dependency array ensures the effect runs only once

  return (
    <>
      <div id="map-container" />
    </>
  );
};

export default MapboxMap;
