import { useEffect, useState } from 'react'

export const App = () => {
  const [ messenge, setMessenge ] = useState()
  
  useEffect(() => {
    const fetchData = async () => {
      const data = await fetch('http://localhost:8701').then((resp)=> resp.json());
      const messengeData = data.message
      setMessenge(messengeData);
    }

    fetchData()
      .catch(console.error);
  }, [])
  
  return (
    <div className="App">
      <h1> { messenge } fcrud</h1>
     
    </div>
  )

}

