(function($) {
  'use strict';
  $(function() {

    if ($("#transactions-chart").length) {
      const ctx = document.getElementById('transactions-chart');
			var graphGradient1 = document.getElementById('transactions-chart').getContext("2d");

			var gradientColor = graphGradient1.createLinearGradient(0, 0, 0, 110);
			gradientColor.addColorStop(0, 'rgba(0, 0, 0, 0)');
			gradientColor.addColorStop(1, 'rgba(243, 153, 21, .6)');
			
      new Chart(ctx, {
        type: 'line',
        data: {
					labels: ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL"],
          datasets: [
            {
              data: [42, 90, 70, 88, 15, 92, 40, 75, 60, 90, 75, 100],
              backgroundColor: gradientColor,
              borderColor: [
                '#f39915'
              ],
              borderWidth: 2,
              fill: 'origin',
              label: "online",
							pointRadius:0,
              tension:0,
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#6C7383",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150
              },
            },
            y: {
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#6C7383",
                beginAtZero: false,
                stepsize:10,
                display:false,
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#sales-chart-a").length) {
      const ctx = document.getElementById('sales-chart-a');
      new Chart(ctx, {
        type: 'line',
        data: {
					labels: ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AI", "AJ", "AK"],
          datasets: [
            {
              data: [30, 38, 20, 30, 25, 35, 19, 23,19, 27],
              backgroundColor: [
                '#003c7c'
              ],
              borderColor: [
                '#003c7c'
              ],
              borderWidth: 1,
              fill: 'origin',
              label: "Sales",
              tension: .35,
							pointRadius:0,
            },
            {
              data: [62, 58, 40, 52, 58, 55, 52, 62, 55, 60],
              backgroundColor: [
                '#2981d7'
              ],
              borderColor: [
                '#2981d7'
              ],
              borderWidth: 1,
              fill: 'origin',
              label: "Orders",
              tension: .35,
							pointRadius:0,
            },
            {
              data: [73, 70, 82, 70, 90, 97, 71, 98, 88, 98],
              backgroundColor: [
                'rgba(207, 220, 237, .8)'
              ],
              borderColor: [
                'rgba(207, 220, 237, .8)'
              ],
              borderWidth: 1,
              fill: 'origin',
              label: "Revenue",
              tension: .35,
							pointRadius:0,
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#6C7383",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150
              },
            },
            y: {
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#6C7383",
                beginAtZero: false,
                stepsize:10,
                display:false,
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#sales-chart-b").length) {
      const ctx = document.getElementById('sales-chart-b');
      new Chart(ctx, {
        type: 'bar',
        data: {
					labels: ['AA', 'AB', 'AC', 'AD', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD'],
          datasets: [
            {
              label: 'Profit',
              data: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,],
              backgroundColor: ['#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', '#3b86d1', 'rgba(180, 213, 246, .8)', 'rgba(180, 213, 246, .8)', 'rgba(180, 213, 246, .8)', 'rgba(180, 213, 246, .8)', 'rgba(180, 213, 246, .8)' ]
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#9fa0a2",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150
              },
            },
            y: {
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#9fa0a2",
                beginAtZero: false,
                stepsize:10,
                display:false,
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#cpu-chart").length) {
      const ctx = document.getElementById('cpu-chart');
      new Chart(ctx, {
        type: 'bar',
        data: {
					labels: ["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L"],
          datasets: [
            {
              label: 'Profit',
              data: [45, 38, 29, 35, 37, 38, 24, 28, 19, 33, 42, 48],
              backgroundColor: '#dc3545',
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#6C7383",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150
              },
            },
            y: {
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#6C7383",
                beginAtZero: false,
                stepsize:10,
                display:false,
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#memory-chart").length) {
      const ctx = document.getElementById('memory-chart');
      new Chart(ctx, {
        type: 'bar',
        data: {
					labels: ["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L"],
          datasets: [
            {
              label: 'Profit',
              data: [38, 35, 23, 22, 35, 23, 24, 28, 19, 33, 30, 45],
              backgroundColor: '#00c8bf',
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#6C7383",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150
              },
            },
            y: {
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#6C7383",
                beginAtZero: false,
                stepsize:10,
                display:false,
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#income-chart").length) {
      const ctx = document.getElementById('income-chart');
      new Chart(ctx, {
        type: 'line',
        data: {
					labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
          datasets: [
            {
              label: 'Register User',
              data: [80, 180, 80, 200, 140, 180, 70],
              borderColor: [
                '#a43cda'
              ],
              borderWidth: 2,
              fill: true,
              backgroundColor: "rgba(164, 60, 218, .1)",
							pointRadius:0,
            },
            {
              label: 'Premium User',
              data: [200, 340, 200, 340, 220, 310, 190],
              borderColor: [
                '#00c8bf'
              ],
              borderWidth: 2,
              fill: true,
              backgroundColor: 'rgba(0, 200, 191, .1)',
							pointRadius:0,
  
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
                color:"#b1b1b5"
              },
              ticks: {
                color: "#b1b1b5",
                display:true,
                beginAtZero: false,
                font: {
                  size: 11,
                  weight: 300,
                }
              },
            },
            y: {
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:true,
              },
              ticks: {
                color: "#b1b1b5",
                beginAtZero: true,
                stepsize: 50,
                stepValue: 50,
                max: 500,
                display:true,
                maxTicksLimit:5,
                font: {
                  size: 11,
                  weight: 300,
                }
                
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
				plugins: [{
          afterDatasetUpdate: function (chart, args, options) {
              const chartId = chart.canvas.id;
              var i;
              const legendId = `${chartId}-legend`;
              const ul = document.createElement('ul');
              for(i=0;i<chart.data.datasets.length; i++) {
                  ul.innerHTML += `
                  <li>
                    <span style="background-color: ${chart.data.datasets[i].borderColor}"></span>
                    ${chart.data.datasets[i].label}
                  </li>
                `;
              }
              return document.getElementById(legendId).appendChild(ul);
            }
        }]
      });

    }

    if ($("#sales-chart-c").length) {
      var salesChartCCanvas = $("#sales-chart-c").get(0).getContext("2d");
      var salesChartC = new Chart(salesChartCCanvas, {
        type: 'pie',
        data: {
          datasets: [{
            data: [20, 20, 60],
            backgroundColor: [
              '#f39915',
              '#21bf06',
              '#a43cda'
            ],
            borderColor: [
              '#f39915',
              '#21bf06',
              '#a43cda'
            ],
            legend:false,
          }],
      
          // These labels appear in the legend and in the tooltips when hovering different arcs
          labels: [
            'Gross Sales',
            'Purchases',
            'Tax Return'
          ]
        },
        options: {
          responsive: true,
          animation: {
            animateScale: true,
            animateRotate: true
          },
          plugins: {
            legend: {
                display: false,
            }
          }
        }
      });
    }
    
    if ($("#sales-chart-d").length) {
      const ctx = document.getElementById('sales-chart-d');
      new Chart(ctx, {
        type: 'bar',
        data: {
					labels: ["2014", "2015", "2016", "2017", "2018", "2019"],
          datasets: [
            {
              label: 'Offline Sales',
              data: [52, 40, 33, 45, 22, 50],
              backgroundColor: '#a43cda',
              barPercentage: .3,
            },
            {
              label: 'Online Sales',
              data: [22, 45, 23, 50, 15, 40],
              backgroundColor: '#f39915',
              barPercentage: .3
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#6C7383",
                display:true,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150,
                font: {
                  size: 10,
                }
              },
            },
            y: {
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#6C7383",
                beginAtZero: false,
                stepsize:10,
                display:true,
                font: {
                  size: 10,
                }
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#expense-chart").length) {
      const ctx = document.getElementById('expense-chart');
      new Chart(ctx, {
        type: 'bar',
        data: {
					labels: ["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"],
          datasets: [
            {
              label: 'Profit',
              data: [35, 38, 29, 35, 37, 38, 24, 28, 19, 33, 42, 48, 33, 33, 29, 27, 29, 38, 31, 28, 23, 24],
              backgroundColor: '#a43cda',
              barPercentage: 0.5
            },
            {
              label: 'Growth',
              data: [35, 38, 29, 35, 37, 38, 24, 28, 19, 33, 42, 48, 33, 33, 29, 27, 29, 38, 31, 28, 23, 24],
              backgroundColor: '#6c7293',
              barPercentage: 0.5
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {

              stacked:true,
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#9fa0a2",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150,
                font: {
                  size: 10,
                }
              },
            },
            y: {
              stacked:true,
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#9fa0a2",
                beginAtZero: false,
                stepsize:10,
                display:false,
                font: {
                  size: 10,
                }
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#budget-chart").length) {
      const ctx = document.getElementById('budget-chart');
      new Chart(ctx, {
        type: 'bar',
        data: {
					labels: ["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"],
          datasets: [
            {
              label: 'Profit',
              data: [35, 38, 29, 35, 37, 38, 24, 28, 19, 33, 42, 48, 33, 33, 29, 27, 29, 38, 31, 28, 23, 24],
              backgroundColor: '#21bf06',
              barPercentage: 0.5
            },
            {
              label: 'Growth',
              data: [35, 38, 29, 35, 37, 38, 24, 28, 19, 33, 42, 48, 33, 33, 29, 27, 29, 38, 31, 28, 23, 24],
              backgroundColor: '#e1e1e2',
              barPercentage: 0.5
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {

              stacked:true,
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#6C7383",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150,
                font: {
                  size: 10,
                }
              },
            },
            y: {
              stacked:true,
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#6C7383",
                beginAtZero: false,
                stepsize:10,
                display:false,
                font: {
                  size: 10,
                }
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($("#balance-chart").length) {
      const ctx = document.getElementById('balance-chart');
      new Chart(ctx, {
        type: 'bar',
        data: {
					labels: ["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"],
          datasets: [
            {
              label: 'Profit',
              data: [35, 38, 29, 35, 37, 38, 24, 28, 19, 33, 42, 48, 33, 33, 29, 27, 29, 38, 31, 28, 23, 24],
              backgroundColor: '#dc3545',
              barPercentage: 0.5
            },
            {
              label: 'Growth',
              data: [35, 38, 29, 35, 37, 38, 24, 28, 19, 33, 42, 48, 33, 33, 29, 27, 29, 38, 31, 28, 23, 24],
              backgroundColor: '#e1e1e2',
              barPercentage: 0.5
            }
          ]
        },
				options: {
          responsive: true,
          maintainAspectRatio: true,
          elements: {
            line: {
                tension: .4,
            }
          },
          scales: {
            x: {

              stacked:true,
              border: {
                display: false
              },
              grid: {
                display: false,
                drawTicks: true,
              },
              ticks: {
                color: "#6C7383",
                display:false,
                beginAtZero: false,
                steps: 100,
                stepValue: 5,
                max: 150,
                font: {
                  size: 10,
                }
              },
            },
            y: {
              stacked:true,
              beginAtZero: true,
              border: {
                display: false
              },
              grid: {
                display:false,
              },
              ticks: {
                color: "#6C7383",
                beginAtZero: false,
                stepsize:10,
                display:false,
                font: {
                  size: 10,
                }
              },
            }
          },
          plugins: {
            legend: {
                display: false,
                labels: {
                    color: 'rgb(255, 99, 132)'
                }
            }
          }
        },
      });

    }

    if ($.cookie('polluxui-pro-banner')!="true") {
      document.querySelector('#proBanner').classList.add('d-flex');
      document.querySelector('.navbar').classList.remove('fixed-top');
    }
    else {
      document.querySelector('#proBanner').classList.add('d-none');
      document.querySelector('.navbar').classList.add('fixed-top');
    }
    
    if ($( ".navbar" ).hasClass( "fixed-top" )) {
      document.querySelector('.navbar-breadcrumb').classList.remove('mt-0');
      document.querySelector('.navbar').classList.remove('pt-5');
    }
    else {
      document.querySelector('.navbar-breadcrumb').classList.add('mt-0');
      document.querySelector('.navbar').classList.add('pt-5');
      document.querySelector('.navbar').classList.add('mt-3');
      
    }
    document.querySelector('#bannerClose').addEventListener('click',function() {
      document.querySelector('#proBanner').classList.add('d-none');
      document.querySelector('#proBanner').classList.remove('d-flex');
      document.querySelector('.navbar').classList.remove('pt-5');
      document.querySelector('.navbar').classList.add('fixed-top');
      document.querySelector('.navbar-breadcrumb').classList.add('proBanner-margin-top');
      document.querySelector('.navbar').classList.remove('mt-3');
      var date = new Date();
      date.setTime(date.getTime() + 24 * 60 * 60 * 1000); 
      $.cookie('polluxui-pro-banner', "true", { expires: date });
    });
    
  });
})(jQuery);