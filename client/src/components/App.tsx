import { FunctionalComponent, h } from "preact";
import { Router, Route } from "preact-router";

import styles from "./App.css";

const App: FunctionalComponent = () => {
  return (
    <div class={styles.container}>
      <Router>
      </Router>
    </div>
  );
};

export default App;
