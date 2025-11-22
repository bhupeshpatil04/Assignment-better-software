
import React, {useEffect, useState} from 'react';

export default function Comments({taskId}){
  const [comments, setComments] = useState([]);
  const [text, setText] = useState('');
  useEffect(()=>{ fetchList(); }, []);
  function fetchList(){
    fetch(`/tasks/${taskId}/comments`).then(r=>r.json()).then(setComments);
  }
  async function add(){
    if(!text) return;
    await fetch(`/tasks/${taskId}/comments`, {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({text, author:'web'})
    });
    setText('');
    fetchList();
  }
  async function del(id){
    await fetch(`/tasks/${taskId}/comments/`+id,{method:'DELETE'});
    fetchList();
  }
  return (
    <div>
      <div>
        <input value={text} onChange={e=>setText(e.target.value)} placeholder="Write comment" />
        <button onClick={add}>Add</button>
      </div>
      <ul>
        {comments.map(c=>(
          <li key={c.id} style={{margin:'8px 0'}}>
            {c.text} <button onClick={()=>del(c.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
