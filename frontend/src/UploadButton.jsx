import React from "react";
import "./UploadButton.css";

import { UploadOutlined } from '@ant-design/icons';
import { Button, Upload } from 'antd';

function UploadButton() {
  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    console.log('アップロードするファイル: ', file.name);
  };
const fileList = [
  {
    uid: '0',
    name: 'xxx.png',
    status: 'uploading',
    percent: 33,
  },
  {
    uid: '-1',
    name: 'yyy.png',
    status: 'done',
    url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
    thumbUrl: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
  },
  {
    uid: '-2',
    name: 'zzz.png',
    status: 'error',
  },
];
  
  return (
    <>
    <Upload
      action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
      listType="picture"
      defaultFileList={[...fileList]}
    >
      <Button icon={<UploadOutlined />}>Upload</Button>
    </Upload>
  </>
  );

  // return (
  //   <div>
  //     <Space
  //   direction="vertical"
  //   style={{
  //     width: '100%',
  //   }}
  // >
  //     <label>
  //       <input
  //         type="file"
  //         id="fileInput"
  //         onChange={handleFileChange}
  //         // style={{ display: 'none' }}
  //         className="upload-button"
  //       />
  //       <label htmlFor="fileInput">
  //         {/* <Button type="primary" block>ファイルをアップロード</Button> */}
  //         <button type="button">ファイルをアップロード</button>
  //       </label>
  //     </label>
  //     </Space>
  //   </div>
  // );
}

export { UploadButton };
