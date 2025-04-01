// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

// tools to control starting operations

#pragma once
#include <filesystem>
#include <string>
#include <string_view>

namespace cma {

enum class AppType { automatic = 99, srv = 0, test, exe, failed };
enum class YamlCacheOp { nothing, update };
namespace env {
constexpr const std::wstring_view test_integration_root{
    L"WNX_TEST_I_ROOT"};  // integration
constexpr const std::wstring_view test_root{L"WNX_TEST_ROOT"};
constexpr const std::wstring_view auto_reload{L"CMA_AUTO_RELOAD"};
}  // namespace env

AppType AppDefaultType();  // defined by main

// must be called on start
bool OnStart(AppType Type = AppType::automatic,
             const std::wstring& ConfigFile = L"");

bool LoadConfigFull(const std::wstring& ConfigFile);
bool LoadConfigBase(const std::vector<std::wstring>& config_filenames,
                    YamlCacheOp cache_op);
bool ReloadConfig();
inline bool OnStartApp() { return OnStart(AppType::automatic); }

inline bool OnStartTest() { return OnStart(AppType::test); }

// recommended to be called on exit. BUT, PLEASE WAIT FOR ALL THREADS/ ASYNC
void OnExit();  // #VIP will stop WMI and all services(in the future)

bool ConfigLoaded();

class UninstallAlert {
public:
    UninstallAlert() = default;
    UninstallAlert(const UninstallAlert&) = delete;
    UninstallAlert(UninstallAlert&&) = delete;
    UninstallAlert& operator=(const UninstallAlert&) = delete;
    UninstallAlert& operator=(UninstallAlert&&) = delete;
    bool isSet() const noexcept {
        return set_;
    }                       // check during exit from the service
    void clear() noexcept;  // test only
    void set() noexcept;    // set when command is got from the
                            // transport
private:
    bool set_ = false;
};

extern UninstallAlert g_uninstall_alert;

std::pair<std::filesystem::path, std::filesystem::path> FindAlternateDirs(
    AppType app_type);

}  // namespace cma
