@echo off

REM Root directory
@REM set ROOT=log_pattern_detection_tool
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\events"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\models"
call :create_folder "%ROOT%\scenarios"
call :create_folder "%ROOT%\simulator"
call :create_folder "%ROOT%\tests"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"

call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\config\__init__.py"
call :create_py_file "%ROOT%\config\config.py"

call :create_py_file "%ROOT%\events\__init__.py"
call :create_py_file "%ROOT%\events\custom_events.py"
call :create_py_file "%ROOT%\events\hospital_events.py"
call :create_py_file "%ROOT%\events\queue_events.py"
call :create_py_file "%ROOT%\events\traffic_events.py"
call :create_py_file "%ROOT%\models\__init__.py"
call :create_py_file "%ROOT%\models\hospital_system.py"
call :create_py_file "%ROOT%\models\generic_system.py"
call :create_py_file "%ROOT%\models\queue_system.py"
call :create_py_file "%ROOT%\models\traffic_system.py"
call :create_py_file "%ROOT%\scenarios\__init__.py"
call :create_py_file "%ROOT%\scenarios\queue_simulation.py"
call :create_py_file "%ROOT%\scenarios\traffic_simulation.py"
call :create_py_file "%ROOT%\simulator\__init__.py"
call :create_py_file "%ROOT%\simulator\engine.py"
call :create_py_file "%ROOT%\simulator\event.py"
call :create_py_file "%ROOT%\simulator\event_queue.py"
call :create_py_file "%ROOT%\simulator\metrics.py"
call :create_py_file "%ROOT%\simulator\utils.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\test_engine.py"
call :create_py_file "%ROOT%\tests\test_events.py"
call :create_py_file "%ROOT%\tests\test_metics.py"
call :create_py_file "%ROOT%\tests\test_event_queue.py"
call :create_py_file "%ROOT%\tests\test_scenarios.py"
call :create_py_file "%ROOT%\tests\test_runner.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\logs\events.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Event-Driven System Simulator Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Event-Driven System Simulator - Simulate real-world event systems ^(traffic, queues^)
echo # Skills: simulation modeling, priority queues
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b