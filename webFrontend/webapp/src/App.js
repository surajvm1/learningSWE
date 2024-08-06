import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './components/Home';
import GetUserData from './components/GetUserData';
import PostUserData from './components/PostUserData';
import TodayWeather from './components/TodayWeather';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            {/* Comment: We could also have like: <li><Link to="/getUserData">Get User Data</Link></li> and so on... */}
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/getUserData" element={<GetUserData />} />
          <Route path="/postUserData" element={<PostUserData />} />
          <Route path="/todayWeather" element={<TodayWeather />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

/*
Function explain:
React makes use of an external library to handle routing; react-router-dom.
<Route path="/" element={<Home />} /> - Renders Home component in that route '/'.
A <Link> is an element that lets the user navigate to another page by clicking or tapping on it. In react-router-dom, a <Link> renders an accessible <a> element with a real href that points to the resource it's linking to.
*/

/*
ReactJS: Basic KT (Reference from: https://github.com/sudheerj/reactjs-interview-questions) + Self doubt questions/answers

React (aka React.js or ReactJS) is an open-source front-end JavaScript library that is used for building composable user interfaces, especially for single-page applications. It is used for handling view layer for web and mobile apps based on components in a declarative approach.

The major features of React are:
Uses JSX syntax, a syntax extension of JS that allows developers to write HTML in their JS code.
It uses Virtual DOM instead of Real DOM considering that Real DOM manipulations are expensive.
Supports server-side rendering which is useful for Search Engine Optimizations(SEO).
Follows Unidirectional or one-way data flow or data binding.
Uses reusable/composable UI components to develop the view.

JSX stands for JavaScript XML and it is an XML-like syntax extension to ECMAScript. Basically it just provides the syntactic sugar for the React.createElement(type, props, ...children) function, giving us expressiveness of JavaScript along with HTML like template syntax.
JSX is stricter than HTML
Eg:
export default function App() {
  return <h1 className="greeting">{"Hello, this is a JSX Code!"}</h1>;
}

An Element is a plain object describing what you want to appear on the screen in terms of the DOM nodes or other components. Elements can contain other Elements in their props. Creating a React element is cheap. Once an element is created, it cannot be mutated.
Eg:
const element = React.createElement("div", { id: "login-btn" }, "Login");
Whereas a component can be declared in several different ways. It can be a class with a render() method or it can be defined as a function. In either case, it takes props as an input, and returns a JSX tree as the output:
Eg:
const Button = ({ handleLogin }) => (
  <div id={"login-btn"} onClick={handleLogin}>
    Login
  </div>
);

Components are the building blocks of creating User Interfaces(UI) in React. There are two possible ways to create a component.
Function Components, Eg:
function Greeting({ message }) {
  return <h1>{`Hello, ${message}`}</h1>;
}
Class Components, Eg:
class Greeting extends React.Component {
  render() {
    return <h1>{`Hello, ${this.props.message}`}</h1>;
  }
}

Use Function Components:
If you don't need state or lifecycle methods, and your component is purely presentational.
For simplicity, readability, and modern code practices, especially with the use of React Hooks for state and side effects.
Use Class Components:
If you need to manage state or use lifecycle methods.
In scenarios where backward compatibility or integration with older code is necessary.

Pure components are the components which render the same output for the same state and props. In function components, you can achieve these pure components through memoized React.memo() API wrapping around the component. This API prevents unnecessary re-renders by comparing the previous props and new props using shallow comparison. So it will be helpful for performance optimizations.

State of a component is an object that holds some information that may change over the lifetime of the component. The important point is whenever the state object changes, the component re-renders. It is always recommended to make our state as simple as possible and minimize the number of stateful components.

Props are inputs to components. They are single values or objects containing a set of values that are passed to components on creation similar to HTML-tag attributes.
The primary purpose of props in React is to provide following component functionality:
Pass custom data to your component.
Trigger state changes.
Use via this.props.reactProp inside component's render() method.

In React, both state and props are plain JavaScript objects and used to manage the data of a component, but they are used in different ways and have different characteristics.
The state entity is managed by the component itself and can be updated using the setter(setState() for class components) function. Unlike props, state can be modified by the component and is used to manage the internal state of the component. i.e, state acts as a component's memory. Moreover, changes in the state trigger a re-render of the component and its children. The components cannot become reusable with the usage of state alone.
On the otherhand, props (short for "properties") are passed to a component by its parent component and are read-only, meaning that they cannot be modified by the own component itself. i.e, props acts as arguments for a function. Also, props can be used to configure the behavior of a component and to pass data between components. The components become reusable with the usage of props.

HTML and React event handling... Synthetic events...

The Virtual DOM (VDOM) is an in-memory representation of Real DOM. The representation of a UI is kept in memory and synced with the "real" DOM. It's a step that happens between the render function being called and the displaying of elements on the screen. This entire process is called reconciliation.

The Virtual DOM works in three simple steps:
Whenever any underlying data changes, the entire UI is re-rendered in Virtual DOM representation.
Then the difference between the previous DOM representation and the new one is calculated. This comparison is done by Diffing Algorithm.
Once the calculations are done, the real DOM will be updated with only the things that have actually changed.

The Shadow DOM is a browser technology designed primarily for scoping variables and CSS in web components. The Virtual DOM is a concept implemented by libraries in JavaScript on top of browser APIs.

Fiber is the new reconciliation engine or reimplementation of core algorithm in React v16. The goal of React Fiber is to increase its suitability for areas like animation, layout, gestures, ability to pause, abort, or reuse work and assign priority to different types of updates; and new concurrency primitives.

The goal of React Fiber is to increase its suitability for areas like animation, layout, and gestures. Its headline feature is incremental rendering: the ability to split rendering work into chunks and spread it out over multiple frames.

A component that controls the input elements within the forms on subsequent user input is called Controlled Component, i.e, every state mutation will have an associated handler function. That means, the displayed data is always in sync with the state of the component.

The Uncontrolled Components are the ones that store their own state internally, and you query the DOM using a ref to find its current value when you need it. This is a bit more like traditional HTML.

When several components need to share the same changing data then it is recommended to lift the shared state up to their closest common ancestor. That means if two child components share the same data from its parent, then move the state to parent instead of maintaining local state in both of the child components.

The attribute class is a keyword in JavaScript, and JSX is an extension of JavaScript. That's the principle reason why React uses className instead of class. Pass a string as the className prop.

It's a common pattern or practice in React for a component to return multiple elements. Fragments let you group a list of children without adding extra nodes to the DOM. You need to use either <Fragment> or a shorter syntax having empty tag (<></>).

Below are the list of reasons to prefer fragments over container DOM elements:
Fragments are a bit faster and use less memory by not creating an extra DOM node. This only has a real benefit on very large and deep trees.
Some CSS mechanisms like Flexbox and CSS Grid have a special parent-child relationships, and adding divs in the middle makes it hard to keep the desired layout.
The DOM Inspector is less cluttered.

Stateless and Stateful component...

The Document Object Model (DOM) is the data representation of the objects that comprise the structure and content of a document on the web.
Server-Side Rendering (SSR) is an approach in which web pages are generated on the server before being sent to the browser. In other words, the server processes the logic and structure of the page and sends the fully rendered page to the user’s browser.
Client-Side Rendering (CSR) involves the browser loading a blank page and then using JavaScript to fill that page with content. In this case, the browser takes a more active role in creating and presenting the user interface.
The <div> tag is used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript. The <div> tag is easily styled by using the class or id attribute.
Class vs Id in HTML: A class name can be used by multiple HTML elements, while an id name must only be used by one HTML element within the page.

The React team worked on extracting all DOM-related features into a separate library called ReactDOM.

React Router is a powerful routing library built on top of React that helps you add new screens and flows to your application incredibly quickly, all while keeping the URL in sync with what's being displayed on the page.

URLSearchParams...

Shallow rendering is useful for writing unit test cases in React. It lets you render a component one level deep and assert facts about what its render method returns, without worrying about the behavior of child components, which are not instantiated or rendered.

Redux is a predictable state container for JavaScript apps based on the Flux design pattern. Redux can be used together with React, or with any other view library. It is tiny (about 2kB) and has no dependencies.

Redux follows three fundamental principles:
Single source of truth: The state of your whole application is stored in an object tree within a single store. The single state tree makes it easier to keep track of changes over time and debug or inspect the application.
State is read-only: The only way to change the state is to emit an action, an object describing what happened. This ensures that neither the views nor the network callbacks will ever write directly to the state.
Changes are made with pure functions: To specify how the state tree is transformed by actions, you write reducers. Reducers are just pure functions that take the previous state and an action as parameters, and return the next state.

More questions about Redux...

React DOM escapes any values embedded in JSX before rendering them. Thus it ensures that you can never inject anything that’s not explicitly written in your application. Everything is converted to a string before being rendered.

*/