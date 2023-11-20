
// WEB 3
const { Web3 } = require('web3');
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/b3a56f2a7d564b41aec9bbb2539e79ff'));

// // Ether
// // TRX Tron Contract
// const abi = [{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"userAddress","type":"address"},{"indexed":false,"internalType":"address payable","name":"relayerAddress","type":"address"},{"indexed":false,"internalType":"bytes","name":"functionSignature","type":"bytes"}],"name":"MetaTransactionExecuted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
// {"inputs":[],"name":"ERC712_VERSION","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PREDICATE_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},
// {"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"userAddress","type":"address"},{"internalType":"bytes","name":"functionSignature","type":"bytes"},{"internalType":"bytes32","name":"sigR","type":"bytes32"},{"internalType":"bytes32","name":"sigS","type":"bytes32"},{"internalType":"uint8","name":"sigV","type":"uint8"}],"name":"executeMetaTransaction","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getChainId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"getDomainSeperator","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getNonce","outputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},
// {"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]

// const address = '0x50327c6c5a14DCaDE707ABad2E27eB517df87AB5'
// // https://web3js.readthedocs.io/en/v1.10.0/web3-eth-contract.html#id29
// const testContract = new web3.eth.Contract(abi, address);
// async function getWeb3Details(){
//     let tokenName = await testContract.methods.name().call()
//     let tokenDecimals = await testContract.methods.decimals().call()
//     let tokenSymbol = await testContract.methods.symbol().call()
//     console.log(tokenName, tokenDecimals, tokenSymbol)
// }

// getWeb3Details()
const { ethers, JsonRpcProvider } =  require('ethers');
const QuoterABI = require('@uniswap/v3-periphery/artifacts/contracts/lens/QuoterV2.sol/QuoterV2.json').abi;


//Read File *******************************
 function getFile(fPath){
    const fs = require('fs')

    try {
        const data = fs.readFileSync(fPath, 'utf-8')
        return data
    } catch (error) {
        console.log('Problem reading the File with the Arbitrage oportunities')
        return console.log('The error '+ error)
    }
}

// Get Price MIO **********************
// async function getPrice(factory, amtIn, tradeDirection) {
//     const provider = new JsonRpcProvider('https://mainnet.infura.io/v3/b3a56f2a7d564b41aec9bbb2539e79ff');
//     const daiAbi = [
//         // Some details about the token
//         "function token0() external view returns (address)",
//         "function token1() external view returns (address)",
//         "function fee() external view returns (uint24)",
    
//         // // Get the account balance
//         // "function balanceOf(address) view returns (uint)",
    
//         // // Send some of your tokens to someone else
//         // "function transfer(address to, uint amount)",
    
//         // // An event triggered whenever anyone transfers to someone else
//         // "event Transfer(address indexed from, address indexed to, uint amount)"
//     ];
//     const daiAddress = factory

//     // The Contract object
//     const poolContract = new ethers.Contract(daiAddress, daiAbi, provider); 
//     let token0Address = await poolContract.token0()
//     let token1Address = await poolContract.token1()
//     let tokenFee = await poolContract.fee()

//     // Get Individual Token information (symbol, name, decimals)
//     let addressArray = [token0Address ,token1Address]
//     let tokenInfoArray = []
//     for (let i = 0; i < addressArray.length; i++) {
//         let tokenAdress = addressArray[1]
//         let tokenAbi = [
//             "function name() view returns (string)",
//             "function symbol() view returns (string)",
//             "function decimals() view returns (uint)",
//         ]
//         let contract = new ethers.Contract(tokenAdress, tokenAbi, provider)
//         let tokenSymbol = await contract.symbol();
//         let tokenName = await contract.name();
//         let tokenDecimals = await contract.decimals();
//         let obj = {
//             id: 'token'+i,
//             tokenSymbol: tokenSymbol,
//             tokenName: tokenName,
//             tokenDecimals: tokenDecimals,
//             tokenAddress: tokenAdress
//         }
//         tokenInfoArray.push(obj)
//     }
//     console.log(tokenInfoArray);

//     // Identify the correct token to unput as A and also B respectively
//     let inputTokenA = ''
//     let inputDecimalsA =0
    
//     let inputTokenB = ''
//     let inputDecimalsB =0

//     if (tradeDirection == 'baseToQuote') {
//         inputTokenA = tokenInfoArray[0].tokenAddress
//         inputDecimalsA = tokenInfoArray[0].tokenDecimals

//         inputTokenB = tokenInfoArray[1].tokenAddress
//         inputDecimalsB = tokenInfoArray[1].tokenDecimals
//     }
    
//     if (tradeDirection == 'quoteToBase') {
//         inputTokenA = tokenInfoArray[1].tokenAddress
//         inputDecimalsA = tokenInfoArray[1].tokenDecimals

//         inputTokenB = tokenInfoArray[0].tokenAddress
//         inputDecimalsB = tokenInfoArray[0].tokenDecimals
//     }

//     //Reformat Amount In
//     if(!isNaN(amtIn)) {
//         amtIn = amtIn.toString()
//     }

//     let amountIn = ethers.parseUnits(amtIn, inputDecimalsA).toString()

//     //Uniswap QuoterV2 Base Address
//     //0x3d4e44Eb1374240CE5F1B871ab261CD16335B76a

//     //Uniswap QuoterV2 Mainnet, Goerli, Arbitrum, Optimism, Polygon Address
//     //0x61fFE014bA17989E743c5F6cB21bF9697530B21e

//     // From the course
//     // 0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6

//     // Get Uniswap V2 swap
//     const quoterAdress = '0x61fFE014bA17989E743c5F6cB21bF9697530B21e'
//     const quoterContract = new ethers.Contract(quoterAdress, QuoterABI, provider); 
//     let quotedAmountOut = 0

//     try {
//         console.log(inputTokenA,inputDecimalsA)
//         console.log(inputTokenB, inputDecimalsB)
//         console.log(amountIn)
//         console.log(tokenFee)

//         quotedAmountOut = await quoterContract.callStatic.quoteExactInputSingle(inputTokenA, inputTokenB, tokenFee, amountIn, 0)
//     } catch (error) {
//         console.log('Catch quoterContract.quoteExactInputSingle')
//         console.log(error)
//         return 0
//     }

//     //Format Output
//     let outputAmount = ethers.formatUnits(quotedAmountOut, inputDecimalsB).toString()
//     console.log('outputAmount')
//     console.log(outputAmount)
// }

// GET PRICE //////////////////////////////
async function getPrice(factory, amtIn, tradeDirection) {

    // Get Provider
    // const provider = new ethers.providers.JsonRpcProvider("https://mainnet.infura.io/v3/29e9ed2bd5cb4248809bf37f2303259e");
    const provider = new JsonRpcProvider('https://mainnet.infura.io/v3/b3a56f2a7d564b41aec9bbb2539e79ff');
    const ABI = [
      'function token0() external view returns (address)',
      'function token1() external view returns (address)',
      'function fee() external view returns (uint24)'
    ];
    const address = factory
  
    // Get Pool Token Information
    const poolContract = new ethers.Contract(address, ABI, provider)
    let token0Address = await poolContract.token0()
    let token1Address = await poolContract.token1()
    let tokenFee = await poolContract.fee()
  
    // Get Individual Token Information (Symbol, Name, Decimals)
    let addressArray = [token0Address, token1Address]
    let tokenInfoArray = []
    for (let i=0; i < addressArray.length; i++) {
      let tokenAddress = addressArray[i]
      let tokenABI = [
        "function name() view returns (string)",
        "function symbol() view returns (string)",
        "function decimals() view returns (uint)"
      ]
      let contract = new ethers.Contract(tokenAddress, tokenABI, provider)
      let tokenSymnol = await contract.symbol()
      let tokenName = await contract.name()
      let tokenDecimals = await contract.decimals()
      let obj = {
        id: "token" + i,
        tokenSymnol: tokenSymnol,
        tokenName: tokenName,
        tokenDecimals: tokenDecimals,
        tokenAddress: tokenAddress
      }
      tokenInfoArray.push(obj)
    }
  
    // Identify the correct token to input as A and also B respectively
    let inputTokenA = ''
    let inputDecimalsA = 0
    let inputTokenB = ''
    let inputDecimalsB = 0
  
    if (tradeDirection == "baseToQuote") {
      inputTokenA = tokenInfoArray[0].tokenAddress
      inputDecimalsA = tokenInfoArray[0].tokenDecimals
      inputTokenB = tokenInfoArray[1].tokenAddress
      inputDecimalsB = tokenInfoArray[1].tokenDecimals
    }
  
    if (tradeDirection == "quoteToBase") {
      inputTokenA = tokenInfoArray[1].tokenAddress
      inputDecimalsA = tokenInfoArray[1].tokenDecimals
      inputTokenB = tokenInfoArray[0].tokenAddress
      inputDecimalsB = tokenInfoArray[0].tokenDecimals
    }
  
    // Reformat Amount In
    if (!isNaN(amtIn)) {amtIn = amtIn.toString()}
    let amountIn = ethers.parseUnits(amtIn, inputDecimalsA).toString()
  
    // Get Uniswap V3 Quote
    const quoterAddress = "0x3d4e44Eb1374240CE5F1B871ab261CD16335B76a";
    const quoterContract = new ethers.Contract(quoterAddress, QuoterABI, provider)
    let quotedAmountOut = 0
    try {
        console.log('quoterContract', {...quoterContract})
        console.log('quoterContract', {...quoterContract.runner})
        console.log('quoterContract', {...quoterContract.functions})
        console.log('quoterContract', {...quoterContract.callStatic})
        console.log('inputTokenA',inputTokenA)
        console.log('inputTokenB',inputTokenB)
        console.log('tokenFee',tokenFee)
        
        quotedAmountOut = await quoterContract.callStatic.quoteExactInputSingle(
            '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
            '0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b',
            3000,
            10000,
            0)

    //   quotedAmountOut = await quoterContract.callStatic.quoteExactInputSingle(
    //     inputTokenA,
    //     inputTokenB,
    //     tokenFee,
    //     amountIn,
    //     0)
        
        console.log('Catch quoterContract.quoteExactInputSingle')
    } catch (error) {
                console.log('Catch quoterContract.quoteExactInputSingle')
                console.log(error)
      return 0
    }
  
      // Format Output
      let outputAmount = ethers.utils.formatUnits(quotedAmountOut, inputDecimalsB).toString()
      return outputAmount
  }

//Read Depth *******************************
async function getDepth(amountIn, limit) 
{
    // Get JSON Surface Rates
  console.log("Reading surface rate information...")
  let fileInfo = getFile("../Uniswap/uniswap_surface_rates.json");
  fileJsonArray = JSON.parse(fileInfo);
  limit = fileJsonArray.length
  fileJsonArrayLimit = fileJsonArray.slice(0, limit);

  // Loop through each trade and get Price information
  for (let i = 0; i < fileJsonArrayLimit.length; i++) {

    // Extract the variables
    let pair1ContractAddress = fileJsonArrayLimit[i].poolContract1
    let pair2ContractAddress = fileJsonArrayLimit[i].poolContract2
    let pair3ContractAddress = fileJsonArrayLimit[i].poolContract3
    let trade1Direction = fileJsonArrayLimit[i].poolDirectionTrade1
    let trade2Direction = fileJsonArrayLimit[i].poolDirectionTrade2
    let trade3Direction = fileJsonArrayLimit[i].poolDirectionTrade3

    // Trade 1
    console.log("Checking trade 1 acquired coin...")
    let acquiredCoinT1 = await getPrice(pair1ContractAddress, amountIn, trade1Direction)

    // // Trade 2
    // console.log("Checking trade 2 acquired coin...")
    // if (acquiredCoinT1 == 0) {return}
    // let acquiredCoinT2 = await getPrice(pair2ContractAddress, acquiredCoinT1, trade2Direction)

    // // Trade 3
    // console.log("Checking trade 3 acquired coin...")
    // if (acquiredCoinT2 == 0) {return}
    // let acquiredCoinT3 = await getPrice(pair3ContractAddress, acquiredCoinT2, trade3Direction)

    // // Calculate Result
    // let result = calculateArbitrage(amountIn, acquiredCoinT3, fileJsonArrayLimit[i])
    
    // console.log("result: " + result)
  }
  return 
}

getDepth(amountIn=1, limit=1)