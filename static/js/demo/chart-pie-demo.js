// Set new default font family and font color to mimic Bootstrap's default styling
(Chart.defaults.global.defaultFontFamily = "Nunito"),
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#858796";

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["Loại 1", "Loại 2", "Loại 3", "Loại 4", "Loại 5", "Loại 6"],
    datasets: [
      {
        data: [10, 20, 10, 20, 10, 30],
        backgroundColor: [
          "#1cc88a",
          "#4e73df",
          "#36b9cc",
          "#f6c23e",
          "#e74a3b",
          "#5a5c69",
        ],
        hoverBackgroundColor: [
          "#2e59d9",
          "#17a673",
          "#2c9faf",
          "#2e59d9",
          "#17a673",
          "#2c9faf",
        ],
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      },
    ],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: "#dddfeb",
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false,
    },
    cutoutPercentage: 80,
  },
});
