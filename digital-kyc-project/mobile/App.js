import React, {useState} from 'react';
import { View, Text, Button, Image, Alert } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function App() {
  const [image, setImage] = useState(null);
  async function pickImage() {
    let result = await ImagePicker.launchCameraAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      quality: 0.8,
    });
    if (!result.cancelled) {
      setImage(result.uri);
      Alert.alert('Captured', 'Image captured. Implement blur/glare checks before upload.');
    }
  }

  return (
    <View style={{flex:1,alignItems:'center',justifyContent:'center'}}>
      <Text>Digital KYC — Mobile Placeholder</Text>
      <Button title="Capture Document / Selfie" onPress={pickImage} />
      {image && <Image source={{uri:image}} style={{width:200,height:300,marginTop:10}} />}
    </View>
  );
}
