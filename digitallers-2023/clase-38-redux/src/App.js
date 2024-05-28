
import { Provider } from 'react-redux';
import './App.css';
//import Contador from './view/componets/Contador';
import Contador from './view/containers/ContadorHook.container';
import store from './store/store';
import Boton from './view/componets/Boton';
import ContadorConnectContainer from './view/containers/ContadorConnect.container';
import Incrementar from './view/containers/IncrementarHook.container';
import Reset from './view/containers/ResetConnect.container';

function App() {
  return (
    <Provider store={store}>
      <div style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh"
      }}>
        <div className='w-50'>
          {/*<Contador valor={5}>*/}
          <Contador>
            <Boton texto="-" />
            <Reset />
            <Incrementar />
          </Contador>

          <ContadorConnectContainer />
        </div>

      </div>
    </Provider>
  );
}

export default App;
