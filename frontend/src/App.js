import React, { useState } from 'react';
let imgFile
function App() {

  const [prediction, setPrediction] = useState([])

  const [file, setFile] = useState();

  const handleFileChange = async (e) => {

    imgFile = e.target.files[0];

    try {
      const base64 = await convertBase64(imgFile)
      setFile(base64);

      console.log("res ===>", base64)

    } catch (e) {

      console.log(e)
    }


  };

  const convertBase64 = (imgFile) => {

    return new Promise((resolve, reject) => {

      const fileReader = new FileReader();
      fileReader.readAsDataURL(imgFile);

      fileReader.onload = (() => {
        resolve(fileReader.result)
      })

      fileReader.onerror = ((error) => {
        reject(error);

      })
    });
  }

  const handleUploadClick = async (e) => {
    e.preventDefault()

    console.log('file===>', file);

    if (!file) {
      return;
    }

    //const img = new FormData();
    //img.append('file2', file);

    const response = await fetch('http://65.0.74.219:5000/test', {
      method: 'POST',
      body: JSON.stringify({
        'file': file
      }),
      headers: {
        'content-type': 'application/json',
        'content-length': `${file.size}`
      }
    })

    const data = await response.json()

    setPrediction([data['id'], data['name'], data['designation'], data['salary']])

    console.log('data===>', data['id'], data['name'], data['designation'], data['salary'])

  }

  //const [id_, name, designation, salary] = prediction;

  return (
    <div align='center'>
      <h1>Deep Learning Project on Image Classification (CNN)</h1>
      This project retrives details of employee based on the image uploaded.
      <hr>
      </hr>
      <body> 
        
      <h1 align='center'>Please upload image of the employee.</h1>

      <form method='post' enctype='multipart/form-data'>
        <input type='file' name="file1" onChange={handleFileChange} />
        {/*<div>{imgFile && `${imgFile.name}-${imgFile.type}`}</div>*/}
        

        <button onClick={handleUploadClick}>Predict</button>
        
      </form>
      
      </body>
      <div >
      <h2>Employee Details</h2>
      <h2>ID          : {prediction[0]}</h2>
      <h2>Name        : {prediction[1]}</h2>
      <h2>Designation : {prediction[2]}</h2>
      <h2>Salary      : {prediction[3]}</h2>
      
      </div>
      <hr />
      <p>This project uses Flask as backend, React.js as frontend and REST api is used to communicate between the Flask and React.<br />
      SQLite is used for storing database.Hosting is done on Amazon Web Services(AWS) EC2 Windows instance. Where Apache(XAMPP)
      is used as a Webserver</p>
      <hr></hr>
      <body>
        
      Designed and Developed by: <u><b>Vipul Sharma</b>.</u> <br />
      E-mail: vipulbharatsharma@gmail.com | Ph. No.: 8278783354 | August, 2023
      
      </body>
      

    </div>
  );


};

export default App;