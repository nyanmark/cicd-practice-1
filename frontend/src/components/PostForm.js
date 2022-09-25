import React,{ useState } from 'react';
import Axios from 'axios';

function PostForm() {
  const url = process.env.REACT_APP_API_URL + "conversion"
  const [data, setData] = useState({
    seconds: "",
    minutes: "",
    degrees: ""
  })
  const [response, setResponse] = useState({})
  const [res_error, setError] = useState({})
  function submit(e){
    e.preventDefault();
    Axios.post(url,{
      seconds: data.seconds,
      minutes: data.minutes,
      degrees: data.degrees
    })
    .then(res => {
      const newres={...res.data}
      setResponse(newres)
      setError({})
      //console.log(newres) //commented for production
    })
    .catch(error => {
      setError(error)
      setResponse({})
      //console.log(error) //commented for production
    })
  }
  function handle(e){
    const newdata={...data}
    newdata[e.target.id] = e.target.value
    setData(newdata)
    //console.log(newdata) //commented for production
    //console.log(url)
  }
  return (
    <div>
        <form onSubmit={(e) => submit(e)}>
            <input onChange={(e) => handle(e)} id='seconds' value={data.seconds} placeholder='seconds' type='number'></input>
            <input onChange={(e) => handle(e)} id='minutes' value={data.minutes} placeholder='minutes' type='number'></input>
            <input onChange={(e) => handle(e)} id='degrees' value={data.degrees} placeholder='degrees' type='number'></input>
            <button>Submit</button>
        </form>
          {res_error.message && <h4><i>{res_error.message}</i> Most Likely Invalid Data Input</h4>}
          {response.degress_result && <h4>Degrees Decimal {response.degress_result}</h4>}
          {response.radians_output && <h4>Radians Result {response.radians_output}</h4>}
    </div>

  )
}

export default PostForm
