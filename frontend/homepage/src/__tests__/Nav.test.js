import React from 'react'
import Nav from '../components/Nav'
import { shallow } from 'enzyme'

describe('Nav Component testing', () => {
  test('Test for  logout button', () => {
    const wrapper = shallow(<Nav />)
    expect(wrapper.find('NavLink')).toBeTruthy()
  })
})