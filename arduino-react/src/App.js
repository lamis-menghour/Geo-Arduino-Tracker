<<<<<<< HEAD
import React from "react";
import MyMap from "./pages/MyMap";

function App() {
  return (
      <MyMap />
=======
// import React, { useState, useEffect } from "react";
// import MyMap from "./MyMap";

// function App() {
//   // Initialize data state with an object that has a 'sensor_value' property
//   const [data, setData] = useState(0);

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         // Use fetch inside useEffect callback
//         const response = await fetch("/location");
//         const newData = await response.json();
//         setData(newData); // Set the 'sensor_value'
//         console.log("newData = ", newData);
//       } catch (error) {
//         console.error("Error fetching data:", error);
//       }
//     };

//     fetchData(); // Call fetchData immediately

//     // If you want to continuously fetch data, you can set up a timer to call fetchData at regular intervals
//     const intervalId = setInterval(fetchData, 500); // Fetch data every 0.5 second (adjust as needed)

//     // Cleanup the interval when the component is unmounted
//     return () => clearInterval(intervalId);
//   }, [setData]); // Dependency array with setData

//   return (
//     <div className="App">
//       {/* Use a conditional rendering to handle the loading state */}
//       {typeof data === "undefined" ? (
//         <p>Loading...</p>
//       ) : (
//         // Render the sensor value
//         <p>GPS data: {data}</p>
//       )}
//       <MyMap />
//     </div>
//   );
// }

// export default App;

import React, { useState, useEffect } from "react";
import MyMap from "./MyMap";

function App() {
  // Initialize data state with an object that has 'Latitude' and 'Longitude' properties
  const [data, setData] = useState({ Latitude: 36.80022, Longitude: 5.744284 });

  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       // Use fetch inside useEffect callback
  //       const response = await fetch("/location");
  //       const newData = await response.json();
  //       setData(newData); // Set the 'Latitude' and 'Longitude'
  //       console.log("newData = ", newData);
  //     } catch (error) {
  //       console.error("Error fetching data:", error);
  //     }
  //   };

  //   fetchData(); // Call fetchData immediately

  //   // If you want to continuously fetch data, you can set up a timer to call fetchData at regular intervals
  //   const intervalId = setInterval(fetchData, 500); // Fetch data every 0.5 second (adjust as needed)

  //   // Cleanup the interval when the component is unmounted
  //   return () => clearInterval(intervalId);
  // }, [setData]); // Dependency array with setData

  return (
    <div className="App">
      {/* Use a conditional rendering to handle the loading state */}
      {data === null ? (
        <p>Loading...</p>
      ) : (
        // Render the GPS data
        <p>
          Latitude {data.Latitude}, Longitude {data.Longitude}
        </p>
      )}
      <MyMap latitude={data.Latitude} longitude={data.Longitude} />
    </div>
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
  );
}

export default App;
