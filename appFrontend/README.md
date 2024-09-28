## Android Dev - React Native

**React Native** is an open-source framework developed by Facebook for building cross-platform mobile applications using JavaScript and React. It enables developers to create apps for both Android and iOS using a single codebase, which significantly reduces development time and effort.

### Key Features of React Native:
1. **Cross-Platform Development:** Write code once and deploy it to both Android and iOS, reducing the need for separate codebases.
2. **Native Performance:** Uses native components under the hood, providing near-native performance.
3. **Live and Hot Reloading:** Allows developers to see changes in the code in real-time without recompiling the entire project.
4. **Modular Architecture:** Provides flexibility by separating code into reusable modules.
5. **Large Community Support:** A thriving community and ecosystem with a wide range of third-party libraries.

------

### React native Questions

1. **What is React Native, and how is it different from React?**

   **Answer:**  
   React Native is a framework developed by Facebook for building cross-platform mobile applications using JavaScript and React. It allows developers to build mobile apps for both iOS and Android using a single codebase.

   - **Difference from React**:
     - React is used for building web applications, whereas React Native is used for building native mobile apps.
     - React Native uses native components like `<View>` and `<Text>` instead of standard HTML elements like `<div>` and `<p>`.
     - React Native bridges JavaScript and native components using a bridge, while React manipulates the DOM directly using the virtual DOM.

2. **What are the core components of React Native?**

   **Answer:**  
   React Native provides several core components for building user interfaces:

   - **View**: A container that supports layout, styling, and touch handling, similar to a `<div>` in HTML.
   - **Text**: Displays text elements, similar to a `<p>` tag in HTML.
   - **Image**: Used to display images from a URL or local resource.
   - **ScrollView**: A scrollable container for long content that doesn't fit on the screen.
   - **TouchableOpacity**: A wrapper for making views respond to touch with a fading effect.
   - **FlatList**: An efficient way to render large lists of data.
   - **SectionList**: Similar to `FlatList`, but used for rendering sections of data with section headers.

3. **What is the purpose of using the `useState` and `useEffect` hooks in React Native?**

   **Answer:**  
   - **useState**:
     - Allows functional components to hold local state.
     - Provides a state variable and a function to update that variable.

   - **Example**:
     ```jsx
     const [count, setCount] = useState(0);
     ```

   - **useEffect**:
     - Allows functional components to perform side effects such as data fetching, subscriptions, or manual DOM manipulations.
     - Can be used to run code when a component mounts, updates, or unmounts.

   - **Example**:
     ```jsx
     useEffect(() => {
       // Run this code on component mount
       console.log("Component mounted");
     }, []); // Empty dependency array means it runs once on mount.
     ```

4. **What is the difference between `State` and `Props` in React Native?**

   **Answer:**  
   - **State**:
     - Local to the component and can change over time.
     - A component can manage its own state and modify it using the `setState` function or `useState` hook.
     - Changing state re-renders the component.

   - **Props**:
     - Short for "properties," and are read-only data passed from a parent component to a child component.
     - Used to pass data and event handlers down to child components.
     - Props are immutable and cannot be changed by the child component.

5. **What are the advantages of using React Native for mobile app development?**

   **Answer:**  
   - **Cross-Platform Development**:
     - Write once, run on both iOS and Android.
     - Share a common codebase for both platforms.

   - **Native Performance**:
     - Uses native components, offering performance similar to native apps.
     - Provides a bridge for direct interaction with native modules and components.

   - **Faster Development**:
     - Hot Reloading allows for instant updates without recompiling.
     - Reusable components speed up development.

   - **Large Community and Ecosystem**:
     - Supported by a large community of developers.
     - Many third-party libraries and components available for integration.

6. **What is Redux, and how is it used in React Native?**

   **Answer:**  
   Redux is a state management library that provides a predictable way to manage the state of your application.

   - **How it Works**:
     - The application state is stored in a single store.
     - The store is updated using actions and reducers.
     - Components connect to the store to access the state or dispatch actions.

   - **Usage in React Native**:
     - Provides a global state that can be accessed and modified by any component in the app.
     - Useful for managing complex state logic, especially in large applications with multiple nested components.

   - **Example Setup**:
     ```jsx
     import { createStore } from 'redux';
     import { Provider } from 'react-redux';

     const store = createStore(rootReducer);

     const App = () => (
       <Provider store={store}>
         <YourComponent />
       </Provider>
     );
     ```

7. **How does navigation work in React Native? Explain the different types of navigation.**

   **Answer:**  
   Navigation in React Native is managed using libraries like `react-navigation` or `react-native-navigation`.

   - **Types of Navigation**:
     - **Stack Navigation**: Manages a stack of screens where each screen is pushed or popped from the stack.
     - **Tab Navigation**: Displays multiple screens using tabs at the bottom or top of the screen.
     - **Drawer Navigation**: Provides a side drawer for navigating between screens.
     - **Nested Navigation**: Combines multiple navigation types to create complex navigation flows.

   - **Example of Stack Navigation**:
     ```jsx
     import { NavigationContainer } from '@react-navigation/native';
     import { createStackNavigator } from '@react-navigation/stack';

     const Stack = createStackNavigator();

     const App = () => (
       <NavigationContainer>
         <Stack.Navigator>
           <Stack.Screen name="Home" component={HomeScreen} />
           <Stack.Screen name="Details" component={DetailsScreen} />
         </Stack.Navigator>
       </NavigationContainer>
     );
     ```

8. **What are some performance optimization techniques in React Native?**

   **Answer:**  
   - **Use `PureComponent` or `React.memo()`**:
     - Prevents unnecessary re-renders of components.

   - **Optimize Images**:
     - Use `Image` with proper dimensions and caching.
     - Consider using libraries like `react-native-fast-image` for optimized image loading.

   - **Avoid Inline Functions and Object Creations**:
     - Move function declarations and object creations outside of the render method.

   - **Use FlatList and SectionList Efficiently**:
     - Use `FlatList` with `keyExtractor`, `getItemLayout`, and `initialNumToRender` to optimize large lists.

   - **Minimize State Updates**:
     - Keep component states as minimal as possible to reduce re-renders.

   - **Enable Hermes**:
     - Use the Hermes JavaScript engine to improve app startup time and memory usage (for Android).

9. **How do you handle different screen sizes and orientations in React Native?**

   **Answer:**  
   - Use `Dimensions` API to get screen width and height:
     ```jsx
     import { Dimensions } from 'react-native';

     const screenWidth = Dimensions.get('window').width;
     const screenHeight = Dimensions.get('window').height;
     ```

   - Use `Platform` API to apply platform-specific styles:
     ```jsx
     import { Platform } from 'react-native';

     const styles = {
       marginTop: Platform.OS === 'ios' ? 20 : 0,
     };
     ```

   - Use `Flexbox` for responsive layouts:
     - Set `flexDirection`, `alignItems`, and `justifyContent` for flexible and responsive designs.

   - Use percentage-based dimensions for styles:
     - Set `width` and `height` as percentages to adapt to different screen sizes.

   - Use media queries with libraries like `react-native-responsive-screen` or `react-native-size-matters` for fine-grained control over screen sizes.

10. **What is the significance of `key` in FlatList or any list rendering in React Native?**

   **Answer:**  
   The `key` prop is used to identify elements in a list uniquely. It helps React Native optimize rendering by determining which items have changed, been added, or been removed.

   - **Why it is important**:
     - Prevents unnecessary re-renders of list items.
     - Improves performance, especially when rendering large lists.
     - Avoids warning messages in the console about missing keys.

   - **Usage Example**:
     ```jsx
     <FlatList
       data={data}
       renderItem={({ item }) => <ItemComponent item={item} />}
       keyExtractor={(item) => item.id.toString()} // Assign a unique key
     />
     ```

---------

Others:

- Setup working condition: Not working. 
- To setup React native project locally, followed below steps:

```
Installed java 11 using sdkman. Install NodeJS. 
Installed Android studio, setup Emulator/virtual device. To check running devices command: adb devices
npm uninstall -g react-native-cli -> As was giving some issues, hence had to uninstall it. 
npx react-native init WeatherAppReactN
cd WeatherAppReactN
npm install @react-navigation/native @react-navigation/native-stack axios
npm install react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context @react-native-community/masked-view 
cd android
./gradlew --version -> To view gradle version 
npx react-native run-android
```
- Though, the setup was giving java related errors - didn't pursue further as otherwise it would break flink related setup I had done in local with running java version.

```
Error:
A problem occurred evaluating project ':app'.
> Failed to apply plugin 'com.android.internal.application'.
   > Android Gradle plugin requires Java 17 to run. You are currently using Java 11.
      Your current JDK is located in /Users/suraj/.sdkman/candidates/java/11.0.23-amzn
      You can try some of the following options:
       - changing the IDE settings.
       - changing the JAVA_HOME environment variable.
       - changing org.gradle.java.home in gradle.properties.

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.
```

---------
