request({
          url: "http://127.0.0.1:5000/weights",
          method: "GET",
          success: (data) => pie_chart(JSON.parse(data)),
          error: () => alert("Failed to connect to server!"),
        });

