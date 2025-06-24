<p align="center"><img src="assets/icon.png" width="200"></p>

# Digital Data Processing Tool

[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)](#) [![Download](https://img.shields.io/badge/Download-Digital%20Data%20Processing%20Tool-brightgreen?style=for-the-badge)](dist/Digital%20Data%20Processing%20Tool.exe)

import React from 'react';
import styled from 'styled-components';

const Button = () => {
  return (
    <StyledWrapper>
      <button className="button">
        Button
      </button>
    </StyledWrapper>
  );
}

const StyledWrapper = styled.div`
  .button {
    position: relative;
    width: 120px;
    height: 40px;
    background-color: #000;
    display: flex;
    align-items: center;
    color: white;
    flex-direction: column;
    justify-content: center;
    border: none;
    padding: 12px;
    gap: 12px;
    border-radius: 8px;
    cursor: pointer;
  }

  .button::before {
    content: '';
    position: absolute;
    inset: 0;
    left: -4px;
    top: -1px;
    margin: auto;
    width: 128px;
    height: 48px;
    border-radius: 10px;
    background: linear-gradient(-45deg, #e81cff 0%, #40c9ff 100% );
    z-index: -10;
    pointer-events: none;
    transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }

  .button::after {
    content: "";
    z-index: -1;
    position: absolute;
    inset: 0;
    background: linear-gradient(-45deg, #fc00ff 0%, #00dbde 100% );
    transform: translate3d(0, 0, 0) scale(0.95);
    filter: blur(20px);
  }

  .button:hover::after {
    filter: blur(30px);
  }

  .button:hover::before {
    transform: rotate(-180deg);
  }

  .button:active::before {
    scale: 0.7;
  }`;

export default Button;



As the name suggests, this tool brings together a range of features, including a number system converter, numeric representations, recursive calculations, and a student records manager — focusing mainly on fundamental concepts taught in the first year of a Computer Science degree.

This is my first experience working on a larger project of this scale and using the Tkinter library, so I’m open to any feedback, suggestions, or support you’d be willing to share. Thanks for checking it out!

## Usage

It’s very simple — just download the .exe file and run it. A window will open, and you’ll be ready to use the tool. Please note that some Windows antivirus programs may flag the .exe as a potentially harmful file, but this is a common false alarm for programs that aren’t digitally signed.
