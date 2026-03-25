const App = () => {
    const [metrics, setMetrics] = React.useState([]);
    const [elements, setElements] = React.useState([]);
    const [chartsData, setChartsData] = React.useState({});
    const [showChartModal, setShowChartModal] = React.useState(false);
    const [showTextModal, setShowTextModal] = React.useState(false);
    const [history, setHistory] = React.useState([[]]);
    const [historyIndex, setHistoryIndex] = React.useState(0);
    const [projectStatus, setProjectStatus] = React.useState('Sin guardar');
    const [lastAction, setLastAction] = React.useState('Ninguna');

    React.useEffect(() => {
        loadMetrics();
    }, []);

    async function loadMetrics() {
        const response = await API.getMetrics();
        setMetrics(response.metrics || []);
    }

    async function loadChartData(metricKey) {
        const data = await API.getMetricData(metricKey);
        if (data) {
            setChartsData(prev => ({ ...prev, [metricKey]: data }));
        }
    }

    function updateHistory(newElements) {
        const newHistory = history.slice(0, historyIndex + 1);
        newHistory.push(newElements);
        setHistory(newHistory);
        setHistoryIndex(newHistory.length - 1);
        setProjectStatus('Sin guardar');
    }

    function addChart(metricKey, chartType) {
        const metric = metrics.find(m => m.key === metricKey);
        const newElement = {
            id: Date.now(),
            type: 'chart',
            metricKey,
            metricLabel: metric?.label || 'Gráfica',
            chartType
        };
        const newElements = [...elements, newElement];
        setElements(newElements);
        updateHistory(newElements);
        loadChartData(metricKey);
        setLastAction(`Gráfica: ${metric?.label}`);
        setShowChartModal(false);
    }

    function addText(content) {
        const newElement = {
            id: Date.now(),
            type: 'text',
            content
        };
        const newElements = [...elements, newElement];
        setElements(newElements);
        updateHistory(newElements);
        setLastAction('Texto agregado');
        setShowTextModal(false);
    }

    function removeElement(id) {
        const newElements = elements.filter(el => el.id !== id);
        setElements(newElements);
        updateHistory(newElements);
        setLastAction('Elemento eliminado');
    }

    function duplicateElement(id) {
        const element = elements.find(el => el.id === id);
        if (element) {
            const newElement = { ...element, id: Date.now() };
            const newElements = [...elements, newElement];
            setElements(newElements);
            updateHistory(newElements);
            setLastAction('Elemento duplicado');
        }
    }

    function editText(id) {
        const content = prompt('Editar texto:');
        if (content !== null) {
            const newElements = elements.map(el =>
                el.id === id ? { ...el, content } : el
            );
            setElements(newElements);
            updateHistory(newElements);
            setLastAction('Texto actualizado');
        }
    }

    function undo() {
        if (historyIndex > 0) {
            const newIndex = historyIndex - 1;
            setHistoryIndex(newIndex);
            setElements(history[newIndex]);
            setLastAction('Deshacer ejecutado');
        }
    }

    function saveProject() {
        setProjectStatus('Guardado');
        setLastAction('Proyecto guardado');
    }

    return React.createElement('div', { className: 'container' },
        React.createElement(Sidebar, {
            onAddChart: () => setShowChartModal(true),
            onAddText: () => setShowTextModal(true),
            onUndo: undo,
            onSave: saveProject,
            projectStatus,
            lastAction
        }),
        React.createElement('div', { className: 'main-content' },
            React.createElement(Header),
            React.createElement(Workspace, {
                elements,
                chartsData,
                onRemove: removeElement,
                onDuplicate: duplicateElement,
                onEditText: editText
            })
        ),
        React.createElement(ChartModal, {
            isOpen: showChartModal,
            metrics,
            onCreate: addChart,
            onClose: () => setShowChartModal(false)
        }),
        React.createElement(TextModal, {
            isOpen: showTextModal,
            onCreate: addText,
            onClose: () => setShowTextModal(false)
        })
    );
};

ReactDOM.render(React.createElement(App), document.getElementById('root'));
