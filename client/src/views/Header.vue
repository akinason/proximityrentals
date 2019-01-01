<template>
  <div id="app">
    <header>
      <section id="one">
        <span>
          <i class="fas fa-bars"></i>
        </span>
        <div class="logo">
          <div class="logo_img">
            <img src="@/assets/logo.png" alt="proximity_rentals">
          </div>
          <p>Proximity Rentals</p>
        </div>
      </section>
    </header>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
}
header {
  background: var(--primary);
  color: var(--white);
  padding: 0.5rem 0;
  display: flex;
  align-items: center;
  position: relative;
  top: 0;
  box-sizing: border-box;
}
header .logo_img {
  width: 3rem;
  height: 3rem;
  overflow: hidden;
}
header img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
header section#one {
  display: flex;
  margin-left: 3rem;
  align-items: center;
}
header section#one span {
  margin-right: 3rem;
  font-size: 1.6rem;
  font-weight: 50;
}
header section#one .logo {
  display: flex;
  flex-basis: 300;
  align-items: center;
  position: relative;
  width: 171px;
}
header section#one .logo .logo_img {
  margin-right: 0.3rem;
}
header section#one .logo p {
  position: absolute;
  right: 0;
  top: 6px;
}
</style>
