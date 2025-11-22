
import React from 'react';
import Comments from './components/Comments';

export default function App(){
  return (
    <div style={{padding:20,fontFamily:'Arial'}}>
      <h2>Tasks - Comments Demo</h2>
      <Comments taskId="task-1" />
    </div>
  );
}
