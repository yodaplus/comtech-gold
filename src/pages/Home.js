import React, { useEffect, useState } from 'react';
import Page from '../components/page';
import {
  Container,
  Typography,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  IconButton,
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  TableContainer,
  Box
} from '@mui/material';

import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import AccordionLayout from '../helpers/AccordionLayout';
import TokenMintingTable from '../components/admin/TokenMintingTable';
import BlacklistAdminTable from '../components/admin/BlacklistAdminTable';
import Contract from 'contracts/ABI.json';
import Web3 from 'web3';

import { useAppState } from '../state/useAppState';

const Home = () => {
  // console.log('🚀 ~ file: Home.js ~ line 25 ~ Contract', Contract.address, Contract.abi);
  // const { abi, address: token } = Contract;
  // const [account, setAccount] = useState('');

  // const web3 = new Web3(Web3.givenProvider);
  // const contract = new web3.eth.Contract(abi, token);

  // const _account = async () => {
  //   const account = await web3.eth.getAccounts().then((accounts) => {
  //     return accounts[0];
  //   });
  //   console.log('🚀 ~ file: Home.js ~ line 38 ~ account ~ account', account);
  //   setAccount(account);
  //   return account;
  // };

  // useEffect(() => {
  //   const acc = _account();
  //   console.log('🚀 ~ file: Home.js ~ line 44 ~ useEffect ~ acc', acc);
  // }, []);
  // console.log('Account: ', account);

  const { account, contract, token } = useAppState();
  console.log('🚀 ~ file: Home.js ~ line 53 ~ Home ~ token', token);
  console.log('🚀 ~ file: Home.js ~ line 53 ~ Home ~ contract', contract);
  console.log('🚀 ~ file: Home.js ~ line 53 ~ Home ~ account', account);

  return (
    <Page title="Admin Dashboard | Comtech Gold">
      <Container>
        <Typography variant="h6" sx={{ fontWeight: 'bold', mt: 2 }}>
          Comtech Gold
        </Typography>
        <Accordion
          defaultExpanded
          sx={{
            boxShadow: 'none',
            border: '1px solid #D2D2D2',
            borderRadius: '6px',
            px: 4,
            py: 1,
            mt: '29px'
          }}
        >
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
            id="panel1a-header"
          >
            <Typography
              sx={{
                fontSize: '1.125rem',
                fontWeight: 'bold'
              }}
            >
              Smart Contracts
            </Typography>
          </AccordionSummary>
          <AccordionDetails>
            <TableContainer>
              <Table size="small" aria-label="a dense table">
                <TableHead>
                  <TableRow>
                    <TableCell>Contract Name</TableCell>
                    <TableCell>Contract Address</TableCell>
                    <TableCell
                      sx={{
                        textAlign: 'center'
                      }}
                    >
                      View On Blocks Scan
                    </TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  <TableRow>
                    <TableCell sx={{ fontWeight: 'bold' }}>Comtech Gold Token</TableCell>
                    <TableCell>
                      <Box
                        sx={{
                          display: 'flex',
                          flexDirection: 'row',
                          m: 0,
                          p: 0,
                          alignItems: 'center'
                        }}
                      >
                        <Box
                          sx={{
                            textOverflow: 'ellipsis',
                            whiteSpace: 'nowrap',
                            overflow: 'hidden'
                          }}
                        >
                          Address
                        </Box>
                        <IconButton aria-label="subs detail" onClick={console.log('copy')}>
                          <ContentCopyIcon sx={{ fontSize: '1rem' }} />
                        </IconButton>
                      </Box>
                    </TableCell>
                    <TableCell
                      sx={{
                        display: 'flex',
                        justifyContent: 'center'
                      }}
                    >
                      AddressFieldTools
                      {/* <AddressFieldTools
                        address={currentNetwork.custodianContractAddress}
                        showInBlockExplorer
                        showAddress={false}
                      /> */}
                    </TableCell>
                  </TableRow>
                  {/* <TableRow>
                    <TableCell sx={{ fontWeight: "bold" }}>
                      Escrow & Settlement
                    </TableCell>
                    <TableCell>
                      <Box
                        sx={{
                          display: "flex",
                          flexDirection: "row",
                          m: 0,
                          p: 0,
                          alignItems: "center",
                        }}
                      >
                        <Box
                          sx={{
                            textOverflow: "ellipsis",
                            whiteSpace: "nowrap",
                            overflow: "hidden",
                          }}
                        >
                          sfg
                        </Box>
                        <IconButton
                          aria-label="subs detail"
                          onClick={console.log("click")}
                        >
                          <ContentCopyIcon sx={{ fontSize: "1rem" }} />
                        </IconButton>
                      </Box>
                    </TableCell>
                    <TableCell
                      sx={{
                        display: "flex",
                        justifyContent: "center",
                      }}
                    >
                      AddressFieldTools
                      <AddressFieldTools
                        address={currentNetwork.escrowManagerAddress}
                        showInBlockExplorer
                        showAddress={false}
                      />
                    </TableCell>
                  </TableRow> */}
                </TableBody>
              </Table>
            </TableContainer>
          </AccordionDetails>
        </Accordion>
        <AccordionLayout title="Token Minting" content={<TokenMintingTable />} />
        <AccordionLayout title="Blacklist Admin" content={<BlacklistAdminTable />} />
      </Container>
    </Page>
  );
};

export default Home;