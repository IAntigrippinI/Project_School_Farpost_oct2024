import './InputFields.css'

const InputFields = ({ description, type, onChange }) => {
    return (
        <div className="auth-inp-field">
            <div className="auth-inp-field-text">
                {description}
            </div>
            <div className="input-field">
                <input className='auth-inp-textarea' onChange={onChange} type={type} ></input>
            </div>
        </div>
    );
}

export default InputFields;