function Sidebar({ history }) {
  return (
    <div className="sidebar">
      <h3>Chat History</h3>
      <ul className="lis">
        {history.map((msg, index) =>
          msg.role === "user" ? (
            <li key={index}>
             {msg.content}
            </li>
          ) : null
        )}
      </ul>
    </div>
  );
}

export default Sidebar;
