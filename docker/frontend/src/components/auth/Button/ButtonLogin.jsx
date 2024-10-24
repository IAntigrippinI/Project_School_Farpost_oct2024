import './ButtonLogin.css'


const ButtonLogin = ({ text, style, onClick }) => {
    return (
        <div className="auth-btn-block">
            <div className={style}>
                <a onClick={onClick}>{text}</a>
            </div>
        </div>
    );
}

export default ButtonLogin;