$(document).ready(() => {

    // Side First Graph (Graduation Status By Total Count)
    $.ajax({
        type: 'GET',
        url: '/getGraduationStatusTypeCount',
        dataType: 'json',
        success(response) {
            console.log("getGraduationStatusTypeCount")
            console.log(response);
            plotGraduationStatusTypeCount(response);
        },
        error(error) {
            console.error(`Error : ${error}`);
        },
    });

    // Side Second Graph (Average Count By Total Count)
    $.ajax({
        type: 'GET',
        url: '/getAverageAgeByCount',
        dataType: 'json',
        success(response) {
            console.log("getAverageAgeByCount")
            console.log(response);
            plotAverageAgeByCount(response);
        },
        error(error) {
            console.error(`Error : ${error}`);
        },
    });


    // Side Third Graph (Drugs By Status Total Count)
    $.ajax({
        type: 'GET',
        url: '/getStatusBasedOnDrug',
        dataType: 'json',
        success(response) {
            console.log("getStatusBasedOnDrug")
            console.log(response);
            plotBasedOnStatusDrug(response)
        },
        error(error) {
            console.error(`Error : ${error}`);
        },
    });

    // Side Fourth Graph (Education By Status Total Count)
    $.ajax({
        type: 'GET',
        url: '/getStatusBasedOnEducation',
        dataType: 'json',
        success(response) {
            console.log("getStatusBasedOnEducation")
            console.log(response);
            plotBasedOnStatusEducation(response)
        },
        error(error) {
            console.error(`Error : ${error}`);
        },
    });
});


function plotGraduationStatusTypeCount(data) {
    statusVal = [];
    count = [];
    for (let i = 0; i < data.length; i++) {
        count[i] = data[i].count;
        statusVal[i] = data[i].status;
    }
    const trace = {
        x: count,
        y: statusVal,
        marker: {},
        type: 'bar',
        orientation: 'h',
        marker: {
            color: 'rgba(255, 99, 71, 1)',
            width: 1,
        },
    };
    var data = [trace];
    const layout = {
        title: 'Count of Participants by Graduation Status',
        xaxis: {
            title: 'Number of Participants',
            titlefont: {
                size: 13,
                color: 'rgb(107, 107, 107)',
            },
            tickfont: {
                size: 13,
                color: 'rgb(107, 107, 107)',
            },
        },
        yaxis: {
            title: 'Gradutaion Status',
            titlefont: {
                size: 13,
                color: 'rgb(107, 107, 107)',
            },
            tickfont: {
                size: 10,
                color: 'rgb(107, 107, 107)',
            },
        },
    };
    Plotly.newPlot('plotGraduationStatusTypeCount', data, layout);
}

function plotAverageAgeByCount(data) {
    ageRange = ['0-17', '18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '>=60'];
    const trace = {
        x: data,
        y: ageRange,
        marker: {},
        type: 'bar',
        orientation: 'h',
        marker: {
            color: 'rgba(255, 99, 71, 1)',
            width: 1,
        },
    };
    var data = [trace];
    const layout = {
        title: 'Count of Participants By Age',
        xaxis: {
            title: 'Number of Participants',
            titlefont: {
                size: 13,
                color: 'rgb(107, 107, 107)',
            },
            tickfont: {
                size: 13,
                color: 'rgb(107, 107, 107)',
            },
        },
        yaxis: {
            title: 'Age of Participants',
            titlefont: {
                size: 13,
                color: 'rgb(107, 107, 107)',
            },
            tickfont: {
                size: 8,
                color: 'rgb(107, 107, 107)',
            },
        },
    };
    Plotly.newPlot('plotAverageAgeByCount', data, layout);
}

function plotBasedOnStatusDrug(data) {
    var grduatedVal = [],
        terminatedVal = [],
        dischargedVal = [],
        completedVal = [];
    var drugsList = []

    for (var i = 0; i < data.length; i++) {
        if (data[i].drug != null) {
            drugsList.push(data[i].drug);
            for (var j = 0; j < data[i].statusList.length; j++) {
                switch (data[i].statusList[j].status) {
                    case "Graduated":
                        grduatedVal.push(data[i].statusList[j].count)
                        break;

                    case "Terminated":
                        terminatedVal.push(data[i].statusList[j].count)
                        break;

                    case "Discharged":
                        dischargedVal.push(data[i].statusList[j].count)
                        break;

                    case "Completed":
                        completedVal.push(data[i].statusList[j].count)
                        break;
                }
            }
        }
    }
    var trace1 = {
        x: drugsList,
        y: grduatedVal,
        name: "Graduated",
        type: 'bar'
    };

    var trace2 = {
        x: drugsList,
        y: terminatedVal,
        name: 'Terminated',
        type: 'bar'
    };

    var trace3 = {
        x: drugsList,
        y: dischargedVal,
        name: "Discharged",
        type: 'bar'
    };

    var trace4 = {
        x: drugsList,
        y: completedVal,
        name: "Completed",
        type: 'bar'
    };

    var data = [trace1, trace2, trace3, trace4];

    var layout = { barmode: 'stack' };

    Plotly.newPlot('plotBasedOnStatusDrug', data, layout);
}

function plotBasedOnStatusEducation(data) {
    var grduatedVal = [],
        terminatedVal = [],
        dischargedVal = [],
        completedVal = [];
    var educationList = []

    for (var i = 0; i < data.length; i++) {
        if (data[i].educaiton != null) {
            educationList.push(data[i].educaiton)
            for (var j = 0; j < data[i].statusList.length; j++) {
                switch (data[i].statusList[j].status) {
                    case "Graduated":
                        grduatedVal.push(data[i].statusList[j].count)
                        break;

                    case "Terminated":
                        terminatedVal.push(data[i].statusList[j].count)
                        break;

                    case "Discharged":
                        dischargedVal.push(data[i].statusList[j].count)
                        break;

                    case "Completed":
                        completedVal.push(data[i].statusList[j].count)
                        break;
                }
            }
        }
    }
    var trace1 = {
        x: educationList,
        y: grduatedVal,
        name: "Graduated",
        type: 'bar'
    };

    var trace2 = {
        x: educationList,
        y: terminatedVal,
        name: 'Terminated',
        type: 'bar'
    };

    var trace3 = {
        x: educationList,
        y: dischargedVal,
        name: "Discharged",
        type: 'bar'
    };

    var trace4 = {
        x: educationList,
        y: completedVal,
        name: "Completed",
        type: 'bar'
    };

    var data = [trace1, trace2, trace3, trace4];

    var layout = { barmode: 'stack' };

    Plotly.newPlot('plotBasedOnStatusEducation', data, layout);
}

function getAge(dateString) {
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}