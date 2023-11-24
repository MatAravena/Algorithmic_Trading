const { ethers, JsonRpcProvider } =  require('ethers');

const { abi: QuoterABI } = require('@uniswap/v3-periphery/artifacts/contracts/lens/QuoterV2.sol/QuoterV2.json');
// const QuoterABI = require('@uniswap/v3-periphery/artifacts/contracts/lens/Quoter.sol/Quoter.json').abi;

// READ FILE //////////////////////////////
function getFile(fPath) {
  const fs = require('fs')

  try {
    const data = fs.readFileSync(fPath, 'utf8')
    return data
  } catch (err) {
    return []
  }
}

// CALCULATE ARB //////////////////////////
function calculateArbitrage(amountIn, amountOut, surfaceObj) {

  // Calculate profit or loss
  let threshold = 0
  let resultArray = [surfaceObj]
  let profitLossPerc = 0
  let profitLoss = amountOut - amountIn
  if (profitLoss > threshold) {
    profitLossPerc = (profitLoss / amountIn) * 100

    // Provide Output Result
    resultArray.push({profitLossPerc: profitLossPerc})
    console.log(resultArray)
  }
  return
}

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

  console.log('token0Address',token0Address)
  console.log('token1Address',token1Address) 

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


  //Uniswap QuoterV2 Base Address
  //0x3d4e44Eb1374240CE5F1B871ab261CD16335B76a
  //Uniswap QuoterV2 Mainnet, Goerli, Arbitrum, Optimism, Polygon Address
  //0x61fFE014bA17989E743c5F6cB21bF9697530B21e
  // From the course
  // 0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6

  // Get Uniswap V3 Quote
  const quoterAddress = "0x3d4e44Eb1374240CE5F1B871ab261CD16335B76a";
  const quoterContract = new ethers.Contract(quoterAddress.toLowerCase(), QuoterABI, provider)
  let quotedAmountOut = 0

  try {

    // const params = {
    //   "tokenIn": inputTokenA,
    //   "tokenOut": inputTokenB,
    //   "amountIn": amountIn,
    //   "fee": tokenFee,
    //   "sqrtPriceLimitX96": 0,
    // }
    const params = {
      tokenIn: inputTokenA.toLowerCase(),
      tokenOut: inputTokenB.toLowerCase(),
      amountIn: amountIn,
      fee: tokenFee,
      sqrtPriceLimitX96: 0,
    }

    quotedAmountOut = await quoterContract.quoteExactInputSingle.call(params) 
    // quotedAmountOut = await quoterContract.callStatic.quoteExactInputSingle(
    //   inputTokenA,  inputTokenB, amountIn,  tokenFee, 0,
    // )

    console.log('quotedAmountOut', quotedAmountOut)
    // returns (
    //     uint256 amountOut,
    //     uint160 sqrtPriceX96After,
    //     uint32 initializedTicksCrossed,
    //     uint256 gasEstimate
    // )

    console.log('quotedAmountOut', quotedAmountOut.amountOut)

  } catch (err) {
    console.log('err', err)
    return 0
  }

    // Format Output
    let outputAmount = ethers.formatUnits(quotedAmountOut.amountOut, inputDecimalsB).toString()
    
    console.log('outputAmount', outputAmount)
    return outputAmount
}

// GET DEPTH //////////////////////////////
async function getDepth(amountIn) {

  // Get JSON Surface Rates
  console.log("Reading surface rate information...")
  let fileInfo = getFile("../Uniswap/uniswap_surface_rates.json");
  fileJsonArray = JSON.parse(fileInfo);
  let limit = fileJsonArray.length
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
    console.log('acquiredCoinT1', acquiredCoinT1)

    // Trade 2
    if (acquiredCoinT1 == 0) {return}
    let acquiredCoinT2 = await getPrice(pair2ContractAddress, acquiredCoinT1, trade2Direction)
    console.log('acquiredCoinT2', acquiredCoinT2)

    // Trade 3
    if (acquiredCoinT2 == 0) {return}
    let acquiredCoinT3 = await getPrice(pair3ContractAddress, acquiredCoinT2, trade3Direction)

    console.log('amountIn', amountIn)
    console.log('acquiredCoinT3', acquiredCoinT3)
    console.log('result', result)

    // Calculate Result
    let result = calculateArbitrage(amountIn, acquiredCoinT3, fileJsonArrayLimit[i])
    console.log('result', result)
  }
  return
}

getDepth(amountIn=100)
