const Sidebar = ({
  onAddChart,
  onAddText,
  onUndo,
  onSave,
  projectStatus,
  lastAction,
}) => {
  return React.createElement(
    "aside",
    { className: "sidebar" },
    React.createElement(
      "div",
      { className: "sidebar-header" },
      React.createElement("h1", null, "Solarformes"),
      React.createElement("p", null, "Argentina"),
    ),
    React.createElement(
      "nav",
      { className: "sidebar-nav" },
      React.createElement(
        "button",
        {
          className: "sidebar-btn",
          onClick: onAddChart,
        },
        "Agregar Gráfica",
      ),
      React.createElement(
        "button",
        {
          className: "sidebar-btn",
          onClick: onAddText,
        },
        "Agregar Texto",
      ),
      React.createElement("div", { className: "sidebar-divider" }),
      React.createElement(
        "button",
        {
          className: "sidebar-btn",
          onClick: onUndo,
        },
        "Deshacer",
      ),
      React.createElement(
        "button",
        {
          className: "sidebar-btn",
          onClick: onSave,
        },
        "Guardar",
      ),
      React.createElement("div", { className: "sidebar-divider" }),
      React.createElement(
        "div",
        { className: "sidebar-status" },
        React.createElement(
          "p",
          null,
          "Estado: ",
          React.createElement("span", null, projectStatus),
        ),
        React.createElement(
          "p",
          null,
          "Última acción: ",
          React.createElement("span", null, lastAction),
        ),
      ),
    ),
  );
};
