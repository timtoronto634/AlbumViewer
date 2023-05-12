import React from "react";
import "./UploadButton.css";

function UploadButton() {
  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    console.log('アップロードするファイル: ', file.name);
  };

  return (
    <div>
      <label>
        <input
          type="file"
          onChange={handleFileChange}
          style={{ display: 'none' }}
          className="upload-button"
        />
        <label htmlFor="fileInput">
          <button type="button">ファイルをアップロード</button>
        </label>
      </label>
    </div>
  );
}

export { UploadButton };
