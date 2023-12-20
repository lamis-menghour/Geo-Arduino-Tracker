import React, { useState, useEffect } from "react";
import MapComponent from "../components/MapComponent";
import axios from "axios";

const ellabs = { longitude: 5.748404, latitude: 36.80425 };
//clc
// "longitude": 5.744754,
// "latitude": 36.810802

//ellabs
// "longitude":  5.748404,
// "latitude": 36.80425

//home
// "longitude":  5.744284,
// "latitude":36.80022

const MyMap = () => {
  const [status, setStatus] = useState({
    isLoading: true,
    isError: false,
    isSuccess: false,
  });

  // Initialize data state with an object that has 'longitude' and 'latitude' properties
  const [data, setData] = useState(ellabs);
  const url = "http://localhost:5000/location";
  const fetchData = async () => {
    setStatus((prev) => ({ ...prev, isLoading: true }));
    try {
      const {data}  = await axios.get(url);
      if (data.error) {
        setStatus((prev) => ({ ...prev, isError: true }));
        return;
      }
      setData(data);
      console.log("data = ", data);
      setStatus((prev) => ({ ...prev, isSuccess: true }));
    } catch (error) {
      setStatus((prev) => ({ ...prev, isError: true }));
    } finally {
      setStatus((prev) => ({ ...prev, isLoading: false }));
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      {status.isLoading && <div>LOADING...</div>}
      {status.isError && <div> {data?.message} </div>}
      {!status.isLoading && status.isSuccess && (
        <MapComponent data={data} fetchData={fetchData} />
      )}
    </>
  );
};

export default MyMap;
