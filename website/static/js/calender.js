var renderedDate = new Date();
var selectedDate = new Date();
var hasSelected = false;

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const renderCalendar = () => {
  renderedDate.setHours(0, 0, 0, 0);
  selectedDate.setHours(0, 0, 0, 0);
  renderedDate.setDate(1);

  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    renderedDate.getFullYear(),
    renderedDate.getMonth() + 1,
    0
  ).getDate();

  const prevLastDay = new Date(
    renderedDate.getFullYear(),
    renderedDate.getMonth(),
    0
  ).getDate();

  const firstDayIndex = renderedDate.getDay();

  const lastDayIndex = new Date(
    renderedDate.getFullYear(),
    renderedDate.getMonth() + 1,
    0
  ).getDay();

  const nextDays = 7 - lastDayIndex - 1;

  document.querySelector(".date h1").innerHTML =
    months[renderedDate.getMonth()];

  document.querySelector(".date p").innerHTML = renderedDate.getFullYear();

  let days = "";
  var nextWeekDate = new Date(
    selectedDate.getFullYear(),
    selectedDate.getMonth(),
    selectedDate.getDate() + 6
  );
  nextWeekDate.setHours(0, 0, 0, 0);

  //generating days in last month
  for (let x = firstDayIndex - 1; x > 0; x--) {
    var forDate = new Date(
      renderedDate.getFullYear(),
      renderedDate.getMonth() - 1,
      prevLastDay - x + 1
    );
    forDate.setHours(0, 0, 0, 0);

    if (forDate >= selectedDate && forDate <= nextWeekDate && hasSelected) {
      days += `<div class="prev-date selected-day">${
        prevLastDay - x + 1
      }</div>`;
    } else {
      days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
    }
  }

  //generating days in this month
  for (let i = 1; i <= lastDay; i++) {
    var forDate = new Date(
      renderedDate.getFullYear(),
      renderedDate.getMonth(),
      i
    );
    forDate.setHours(0, 0, 0, 0);
    if (forDate >= selectedDate && forDate <= nextWeekDate && hasSelected) {
      days += `<div class="day-date selected-day">${i}</div>`;
    } else {
      days += `<div class="day-date">${i}</div>`;
    }
  }

  //generating days in next month
  for (let j = 1; j <= nextDays + 1; j++) {
    var forDate = new Date(
      renderedDate.getFullYear(),
      renderedDate.getMonth() + 1,
      j
    );
    forDate.setHours(0, 0, 0, 0);
    if (forDate >= selectedDate && forDate <= nextWeekDate && hasSelected) {
      days += `<div class="next-date selected-day">${j}</div>`;
    } else {
      days += `<div class="next-date">${j}</div>`;
    }
  }

  monthDays.innerHTML = days;

  // on clicked date
  var day_dates = document.querySelectorAll(".day-date");
  day_dates.forEach((day_date) => {
    day_date.addEventListener("click", () => setInput(day_date));
  });
};

// function that will set the input values to the selected date
function setInput(day_date) {
  hasSelected = true;

  selectedDate.setFullYear(renderedDate.getFullYear());
  selectedDate.setMonth(renderedDate.getMonth());
  selectedDate.setDate(day_date.textContent);

  var beginDateInput = document.getElementById("begin-date");
  beginDateInput.setAttribute(
    "value",
    selectedDate.getFullYear() +
      "-" +
      selectedDate.getMonth() +
      "-" +
      selectedDate.getDate()
  );
  var endDateInput = document.getElementById("end-date");

  var selectedEndDate = new Date(
    selectedDate.getFullYear(),
    selectedDate.getMonth(),
    selectedDate.getDate() + 6
  );
  selectedEndDate.setHours(0, 0, 0, 0);

  endDateInput.setAttribute(
    "value",
    selectedEndDate.getFullYear() +
      "-" +
      selectedEndDate.getMonth() +
      "-" +
      selectedEndDate.getDate()
  );
  renderCalendar();
}

document.querySelector(".prev").addEventListener("click", () => {
  renderedDate.setMonth(renderedDate.getMonth() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  renderedDate.setMonth(renderedDate.getMonth() + 1);
  renderCalendar();
});

renderCalendar();
