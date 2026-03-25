const ChartElement = ({ element, data, onRemove, onDuplicate, chartRef }) => {
  React.useEffect(() => {
    if (chartRef.current && data) {
      renderChart(chartRef.current, element, data);
    }
  }, [element, data]);

  return React.createElement(
    "div",
    { className: "element" },
    React.createElement(
      "div",
      { className: "element-header" },
      React.createElement(
        "div",
        null,
        React.createElement(
          "div",
          { className: "element-title" },
          element.metricLabel,
        ),
        React.createElement(
          "div",
          { className: "element-subtitle" },
          "Banco Mundial - Argentina",
        ),
      ),
      React.createElement(
        "div",
        { className: "element-actions" },
        React.createElement(
          "button",
          {
            className: "btn-action",
            onClick: () => onDuplicate(element.id),
            title: "",
          },
          "Duplicar",
        ),
        React.createElement(
          "button",
          {
            className: "btn-action delete",
            onClick: () => onRemove(element.id),
            title: "",
          },
          "Eliminar",
        ),
      ),
    ),
    React.createElement(
      "div",
      { className: "chart-container" },
      React.createElement("canvas", { ref: chartRef }),
    ),
  );
};

const TextElement = ({ element, onRemove, onEdit }) => {
  return React.createElement(
    "div",
    { className: "element" },
    React.createElement(
      "div",
      { className: "element-header" },
      React.createElement("div", { className: "element-subtitle" }, "TEXTO"),
      React.createElement(
        "div",
        { className: "element-actions" },
        React.createElement(
          "button",
          {
            className: "btn-action",
            onClick: () => onEdit(element.id),
            title: "Editar",
          },
          "Editar",
        ),
        React.createElement(
          "button",
          {
            className: "btn-action delete",
            onClick: () => onRemove(element.id),
            title: "Eliminar",
          },
          "Eliminar",
        ),
      ),
    ),
    React.createElement("div", { className: "text-content" }, element.content),
  );
};

const Workspace = ({
  elements,
  chartsData,
  onRemove,
  onDuplicate,
  onEditText,
}) => {
  const chartRefs = React.useRef({});

  return React.createElement(
    "div",
    { className: "workspace" },
    React.createElement(
      "div",
      { className: "workspace-inner" },
      elements.length === 0
        ? React.createElement(
            "div",
            { className: "empty-state" },
            React.createElement("h3", null, "Empieza a crear"),
            React.createElement(
              "p",
              null,
              "Selecciona una opción del menú para agregar gráficas o texto",
            ),
          )
        : elements.map((el) => {
            if (el.type === "chart") {
              if (!chartRefs.current[el.id]) {
                chartRefs.current[el.id] = React.createRef();
              }
              return React.createElement(ChartElement, {
                key: el.id,
                element: el,
                data: chartsData[el.metricKey],
                onRemove,
                onDuplicate,
                chartRef: chartRefs.current[el.id],
              });
            } else {
              return React.createElement(TextElement, {
                key: el.id,
                element: el,
                onRemove,
                onEdit: onEditText,
              });
            }
          }),
    ),
  );
};

function renderChart(canvas, element, data) {
  const ctx = canvas.getContext("2d");

  if (window.chartInstances && window.chartInstances[element.id]) {
    window.chartInstances[element.id].destroy();
  }

  const labels = data.data.map((d) => d.year);
  const values = data.data.map((d) => d.value);

  const chartConfig = {
    type: element.chartType,
    data: {
      labels,
      datasets: [
        {
          label: data.label,
          data: values,
          borderColor: CONFIG.COLORS.primary,
          backgroundColor:
            element.chartType === "doughnut"
              ? CONFIG.CHART_COLORS
              : "rgba(143, 191, 143, 0.1)",
          borderWidth: 2,
          tension: 0.4,
          fill: element.chartType === "area",
          borderRadius: 4,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: element.chartType === "doughnut" },
      },
      scales:
        element.chartType === "doughnut"
          ? {}
          : {
              y: { beginAtZero: true },
              x: { grid: { display: false } },
            },
    },
  };

  if (!window.chartInstances) window.chartInstances = {};
  window.chartInstances[element.id] = new Chart(ctx, chartConfig);
}
