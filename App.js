// App.js
import 'react-native-gesture-handler';
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { GestureHandlerRootView } from 'react-native-gesture-handler';

// Import screens
import LandingScreen from './screens/LandingScreen';
import OnboardingScreen from './screens/OnboardingScreen';
import WelcomeScreen from './screens/WelcomeScreen';
import HomeScreen from './screens/HomeScreen';
import ChatScreen from './screens/ChatScreen';
import MeditationScreen from './screens/MeditationScreen';
import SettingsScreen from './screens/SettingsScreen';
import { DrawerContent } from './components/DrawerContent';

const Stack = createNativeStackNavigator();
const Drawer = createDrawerNavigator();

function MainDrawer({ route }) {
  const userDetails = route?.params?.userDetails;
 
  return (
    <Drawer.Navigator
      drawerContent={props => <DrawerContent {...props} />}
      screenOptions={{
        headerShown: false,
        drawerStyle: {
          width: '85%',
        },
      }}
      initialParams={{ userDetails }}
    >
      <Drawer.Screen 
        name="HomeScreen" 
        component={HomeScreen}
        initialParams={{ userDetails }}
        options={{
          unmountOnBlur: true
        }}
      />
      <Drawer.Screen 
        name="Meditation" 
        component={MeditationScreen}
        initialParams={{ userDetails }}
        options={{
          unmountOnBlur: true
        }}
      />
      <Drawer.Screen 
        name="Settings" 
        component={SettingsScreen}
        initialParams={{ userDetails }}
        options={{
          unmountOnBlur: true
        }}
      />
      <Drawer.Screen 
        name="Companion" 
        component={ChatScreen}
        initialParams={{ mode: 'companion', userDetails }} 
        options={{
          unmountOnBlur: true
        }}
      />
      <Drawer.Screen 
        name="TalkToUs" 
        component={ChatScreen}
        initialParams={{ mode: 'support', userDetails }} 
        options={{
          unmountOnBlur: true
        }}
      />
    </Drawer.Navigator>
  );
}

function App() {
  return (
    <SafeAreaProvider>
      <GestureHandlerRootView style={{ flex: 1 }}>
        <NavigationContainer>
          <StatusBar style="auto" />
          <Stack.Navigator
            screenOptions={{
              headerShown: false,
              gestureEnabled: false
            }}
          >
            <Stack.Screen 
              name="Landing" 
              component={LandingScreen}
              options={{
                animationTypeForReplace: 'pop'
              }}
            />
            <Stack.Screen name="Onboarding" component={OnboardingScreen} />
            <Stack.Screen name="Welcome" component={WelcomeScreen} />
            <Stack.Screen 
              name="MainApp" 
              component={MainDrawer}
              options={{
                animationTypeForReplace: 'pop'
              }}
            />
          </Stack.Navigator>
        </NavigationContainer>
      </GestureHandlerRootView>
    </SafeAreaProvider>
  );
}

export default App;

