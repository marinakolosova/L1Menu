import FWCore.ParameterSet.Config as cms

from L1TriggerDPG.L1Menu.customL1Ntuple_cfg import *

process.p.remove(process.l1RecoTreeProducer)
#process.p.remove(process.l1MuonRecoTreeProducer)

process.p.remove(process.gtEvmDigis)

process.l1MuonRecoTreeProducer.runOnPostLS1 = True # CB hack for now so that pre and post LS1 have same muon config
process.l1MuonRecoTreeProducer.triggerMatching = True

# edit here
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

readFiles.extend( ['file:///afs/cern.ch/user/p/pellicci/data2/L1DPG/root/Cosmics_SP_238492_RAWRECO.root'] )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.threshold = 'ERROR'
