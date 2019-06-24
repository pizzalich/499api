export const itomatoGetData = () => {
  const data = fetch("https://itomato-server.herokuapp.com/crud")
    .then(response => response.json())
    .then(data => {
      return data;
    })
    .catch(err => console.log(err));
  return data;
};

export const itomatoPostData = (
  temp = 999,
  humidity = -1,
  light = -1,
  moisture = -1
) => {
  fetch("https://itomato-server.herokuapp.com/crud", {
    method: "post",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      temp: temp,
      humidity: humidity,
      light: light,
      moisture: moisture
    })
  })
    .then(response => response.json())
    .then(item => {
      if (Array.isArray(item)) {
        console.log(item);
      } else {
        console.log("data type error");
      }
    })
    .catch(err => console.log(err));
};

export const itomatoGetImage = () => {
  //TODO THIS IS BROKEN
  const data = fetch("https://itomato-server.herokuapp.com/crud/image")
    .then(response => response.json())
    .then(data => {
      return data;
    })
    .catch(err => console.log(err));
  return data;
};

export const itomatoPostImage = (image = {}) => {
  //TODO THIS IS BROKEN
  fetch("https://itomato-server.herokuapp.com/crud/image", {
    method: "post",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      image: image
    })
  })
    .then(response => response.json())
    .then(item => {
      if (Array.isArray(item)) {
        console.log(item);
      } else {
        console.log("data type error");
      }
    })
    .catch(err => console.log(err));
};
