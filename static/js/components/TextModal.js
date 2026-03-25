const TextModal = ({ isOpen, onCreate, onClose }) => {
    const [textContent, setTextContent] = React.useState('');

    const handleCreate = () => {
        if (textContent.trim()) {
            onCreate(textContent);
            setTextContent('');
        }
    };

    return React.createElement('div', {
        className: `modal-overlay ${isOpen ? 'active' : ''}`
    },
        React.createElement('div', { className: 'modal-content' },
            React.createElement('div', { className: 'modal-header' },
                React.createElement('h3', null, 'Agregar Texto')
            ),
            React.createElement('div', { className: 'form-group' },
                React.createElement('label', { className: 'form-label' }, 'Contenido'),
                React.createElement('textarea', {
                    className: 'form-textarea',
                    value: textContent,
                    onChange: (e) => setTextContent(e.target.value),
                    rows: 6,
                    placeholder: 'Escribe tu texto aquí...'
                })
            ),
            React.createElement('div', { className: 'modal-actions' },
                React.createElement('button', {
                    className: 'btn btn-secondary',
                    onClick: onClose
                }, 'Cancelar'),
                React.createElement('button', {
                    className: 'btn btn-primary',
                    onClick: handleCreate
                }, 'Agregar')
            )
        )
    );
};
