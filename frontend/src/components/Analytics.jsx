import React, { useEffect, useState } from "react";

function Analytics(){

const [data,setData] = useState(null);

useEffect(()=>{

fetch("http://127.0.0.1:8000/analytics")
.then(res=>res.json())
.then(data=>setData(data))

},[])

if(!data) return <div>Loading...</div>

return(

<div>

<h2>Chatbot Analytics</h2>

<p>Total Chats: {data.total_chats}</p>

<p>Total Leads: {data.total_leads}</p>

<h3>Top Products</h3>

<ul>

{data.top_products.map((p,i)=>(
<li key={i}>
{p.product} - {p.count}
</li>
))}

</ul>

</div>

)

}

export default Analytics;