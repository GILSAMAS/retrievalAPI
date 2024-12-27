import App from "./App";
import AppRouter from "./AppRouter";
import { AppProvider } from "./AppContextProvider";
function AppHookContainer() {
    return (
        <AppProvider>
            <App>
                <AppRouter />
            </App>
        </AppProvider>
    );
}

export default  AppHookContainer;