'use strict';

describe('Controller: TestimoniosCtrl', function () {

  // load the controller's module
  beforeEach(module('pi1App'));

  var TestimoniosCtrl,
  scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    TestimoniosCtrl = $controller('TestimoniosCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(TestimoniosCtrl.awesomeThings.length).toBe(3);
  });
});