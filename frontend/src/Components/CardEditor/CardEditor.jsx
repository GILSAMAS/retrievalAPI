import React, { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import './CardEditor.css';

function CardEditor({ onAddCard }) {
  const [front, setFront] = useState('');
  const [back, setBack] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddCard({ front, back });
    setFront('');
    setBack('');
  };

  return (
    <form className="card-editor" onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="front">Front</label>
        <input
          type="text"
          id="front"
          value={front}
          onChange={(e) => setFront(e.target.value)}
          placeholder="Front"
        />
      </div>
      <div className="form-group">
        <label htmlFor="back">Back</label>
        <ReactQuill
          value={back}
          onChange={setBack}
          placeholder="Back"
          modules={{
            toolbar: [
              [{ 'font': [] }, { 'size': [] }],
              ['bold', 'italic', 'underline', 'strike'],
              [{ 'color': [] }, { 'background': [] }],
              [{ 'align': [] }],
              ['clean']
            ]
          }}
        />
      </div>
      <button type="submit">Add Card</button>
    </form>
  );
}

export default CardEditor;