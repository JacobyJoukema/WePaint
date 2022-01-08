import { FunctionalComponent, h } from "preact";
import { Router, Route } from "preact-router";

import Main from "./Main";

const App: FunctionalComponent = () => {
  return (
    <Router>
      {/*<Route path="/" component={Landing} /> */}
      <Route path="/:channel" component={Main} />
    </Router>
  );
};

export default App;
