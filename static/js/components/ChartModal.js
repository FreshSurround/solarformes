const ChartModal = ({ isOpen, metrics, onCreate, onClose, onMetricChange, onTypeChange }) => {
    const [selectedMetric, setSelectedMetric] = React.useState(
        metrics.length > 0 ? metrics[0].key : ''
    );
    const [selectedType, setSelectedType] = React.useState('line');

    React.useEffect(() => {
        if (metrics.length > 0 && !selectedMetric) {
            setSelectedMetric(metrics[0].key);
        }
    }, [metrics]);

    const handleCreate = () => {
        onCreate(selectedMetric, selectedType);
    };

    return React.createElement('div', {
        className: `modal-overlay ${isOpen ? 'active' : ''}`
    },
        React.createElement('div', { className: 'modal-content' },
            React.createElement('div', { className: 'modal-header' },
                React.createElement('h3', null, 'Crear Gráfica')
            ),
            React.createElement('div', { className: 'form-group' },
                React.createElement('label', { className: 'form-label' }, 'Métrica'),
                React.createElement('select', {
                    className: 'form-select',
                    value: selectedMetric,
                    onChange: (e) => setSelectedMetric(e.target.value)
                },
                    metrics.map(m => React.createElement('option', { key: m.key, value: m.key }, m.label))
                )
            ),
            React.createElement('div', { className: 'form-group' },
                React.createElement('label', { className: 'form-label' }, 'Tipo de Gráfica'),
                React.createElement('div', { className: 'chart-type-grid' },
                    CONFIG.CHART_TYPES.map(type =>
                        React.createElement('button', {
                            key: type.key,
                            className: `chart-type-btn ${selectedType === type.key ? 'active' : ''}`,
                            onClick: () => setSelectedType(type.key)
                        }, type.label)
                    )
                )
            ),
            React.createElement('div', { className: 'modal-actions' },
                React.createElement('button', {
                    className: 'btn btn-secondary',
                    onClick: onClose
                }, 'Cancelar'),
                React.createElement('button', {
                    className: 'btn btn-primary',
                    onClick: handleCreate
                }, 'Crear')
            )
        )
    );
};
