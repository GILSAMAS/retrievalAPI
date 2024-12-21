// import { useState, useEffect } from 'react';

// function useAPI({method, url, body}) {
//   const [data, setData] = useState(null);
//   const [error, setError] = useState(null);
//   const [loading, setLoading] = useState(false);

//   useEffect(() => {
//     setLoading(true);
//     setError(null);

//     fetch(url, {
//       method,
//       body: JSON.stringify(body),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     })
//       .then(response => response.json())
//       .then(data => setData(data))
//       .catch(error => setError(error))
//       .finally(() => setLoading(false));
//   }, [method, url, body]);

//   return { data, error, loading };
// }

// export default useAPI;

import { useState, useEffect } from 'react';

function useAPI({ method, url, body }, shouldFetch) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!shouldFetch || !url || !method) return;

    setLoading(true);
    setError(null);

    fetch(url, {
      method,
      body: body ? JSON.stringify(body) : null,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setData(data))
      .catch((error) => setError(error))
      .finally(() => setLoading(false));
  }, [method, url, body, shouldFetch]);

  return { data, error, loading };
}

export default useAPI;
