import React from 'react';

function ImageInput() {
  return (
    <div>
      <input type="file" accept="image/*" /> {/* Placeholder input for image upload */}
    </div>
  );
}

export default ImageInput;