import envs from "../../envs.json";

var payjpInstance = null;

export const useCreditCardForm = () => {

  let payjp = (()=>{
    if (payjpInstance == null) {
      payjpInstance = Payjp(envs.payjpPubKey)
    } 
    return payjpInstance    
  })()

  const numberStyle = {
    base: {
      letterSpacing: '0.08rem',
      lineHeight: '56px',
    },
    invalid: {
      color: '#DF5475',
    },
    complete: {
      color: '#205EFB',
    }
  };

  const generateForm = () => {
    const elements = payjp.elements()
    const number = elements.create('cardNumber', { style: numberStyle })
    const expiry = elements.create('cardExpiry', { style: numberStyle })
    const cvc    = elements.create('cardCvc', { style: numberStyle })
    return { number, expiry, cvc }
  }

  return { payjp, generateForm }
}
