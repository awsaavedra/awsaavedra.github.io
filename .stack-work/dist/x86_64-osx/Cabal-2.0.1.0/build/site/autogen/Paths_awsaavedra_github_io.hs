{-# LANGUAGE CPP #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -fno-warn-implicit-prelude #-}
module Paths_awsaavedra_github_io (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/Alexander/workspace/awsaavedra.github.io/.stack-work/install/x86_64-osx/lts-10.3/8.2.2/bin"
libdir     = "/Users/Alexander/workspace/awsaavedra.github.io/.stack-work/install/x86_64-osx/lts-10.3/8.2.2/lib/x86_64-osx-ghc-8.2.2/awsaavedra-github-io-0.1.0.0-7676robcEXOCzq6Spwz6O0-site"
dynlibdir  = "/Users/Alexander/workspace/awsaavedra.github.io/.stack-work/install/x86_64-osx/lts-10.3/8.2.2/lib/x86_64-osx-ghc-8.2.2"
datadir    = "/Users/Alexander/workspace/awsaavedra.github.io/.stack-work/install/x86_64-osx/lts-10.3/8.2.2/share/x86_64-osx-ghc-8.2.2/awsaavedra-github-io-0.1.0.0"
libexecdir = "/Users/Alexander/workspace/awsaavedra.github.io/.stack-work/install/x86_64-osx/lts-10.3/8.2.2/libexec/x86_64-osx-ghc-8.2.2/awsaavedra-github-io-0.1.0.0"
sysconfdir = "/Users/Alexander/workspace/awsaavedra.github.io/.stack-work/install/x86_64-osx/lts-10.3/8.2.2/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "awsaavedra_github_io_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "awsaavedra_github_io_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "awsaavedra_github_io_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "awsaavedra_github_io_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "awsaavedra_github_io_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "awsaavedra_github_io_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
