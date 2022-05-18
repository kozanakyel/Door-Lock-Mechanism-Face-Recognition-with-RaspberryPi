
  
import React from "react";
//import { connect } from "react-redux";

const Home = () => {
  return (
    <div className="container">
      <div className="row d-flex flex-column">
       
        <div className="col-md-10 mx-auto my-4">
          <table className="table table-hover">
            <thead className="table-header bg-dark text-white">
              <tr>
                <th scope="col">Id</th>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Entry Time</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
                  <tr>
                    <td>{'1'}</td>
                    <td>{'vesile'}</td>
                    <td>{'vesile@gmail.com'}</td>
                    <td>{'15.05.2022'}</td>                    
                  </tr>
                  <tr>
                    <td>{'2'}</td>
                    <td>{'Ugur'}</td>
                    <td>{'ugur@gmail.com'}</td>
                    <td>{'16.05.2022'}</td>                    
                  </tr>
                  <tr>
                    <td>{'3'}</td>
                    <td>{'simge'}</td>
                    <td>{'simge@gmail.com'}</td>
                    <td>{'17.05.2022'}</td>                    
                  </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};


export default Home;