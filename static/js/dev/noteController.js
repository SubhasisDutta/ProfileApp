'use strict';

/**
 * The root conferenceApp module.
 *
 * @type {noteApp|*|{}}
 */
var noteApp = noteApp || {};

/**
 * @ngdoc module
 * @name noteControllers
 *
 * @description
 * Angular module for controllers.
 *
 */
noteApp.controllers = angular.module('noteControllers', ['ui.bootstrap']);


/**
 * @ngdoc controller
 * @name HomeSliderCtrl
 *
 */
noteApp.controllers.controller('HomeSliderCtrl', function ($scope) {		
	  $scope.myInterval = 3000;
	  $scope.slides = [
	    {
	    	image : 'temp/homeslide/alltiles.jpg', 
			title : 'Scroll to see some of these projects 1',
			link : '#/viewnote/keyID1'
	    },
	    {
	    	image : 'temp/homeslide/xspowerrobots.jpg', 
	    	title : 'Scroll to see some of these projects 2',
			link : '#/viewnote/keyID2'
	    },
	    {
	      image: 'http://lorempixel.com/400/200/sports',
	      title : 'Scroll to see some of these projects 3',
		  link : '#/viewnote/keyID3'
	    },
	    {
	      image: 'http://lorempixel.com/400/200/people',
	      title : 'Scroll to see some of these projects 4',
		  link : '#/viewnote/keyID4'
	    },
	    {
	    	image : 'temp/homeslide/xspowerrobots.jpg', 
	    	title : 'Scroll to see some of these projects 5',
			link : '#/viewnote/keyID5'
	    }
	  ];	
});


noteApp.controllers.controller('NoteCategoryCtrl', function ($scope) {
	  $scope.notes = [
	    {
	    	handle: 'Keyno1',
	    	title : 'Integrate with your local directory 1',
	    	icon : '/img/business2.jpg',
	    	image : 'temp/homeslide/alltiles.jpg', 
	    	summery : 'Use the same user accounts and groups in the cloud that you already use on Use the same user accounts and groups in the cloud that you already use on premises. Use the same user accounts and groups in the cloud that you already use on premises.',			
	    },
	    {
	    	handle: 'Keyno2',
	    	title : 'Integrate with your local directory 2',
	    	icon : '/img/business2.jpg',
	    	image : 'temp/homeslide/alltiles.jpg', 
	    	summery : 'Use the same user accounts and groups in the cloud that you already use on Use the same user accounts and groups in the cloud that you already use on premises. Use the same user accounts and groups in the cloud that you already use on premises.',			
	    },
	    {
	    	handle: 'Keyno3',
	    	title : 'Integrate with your local directory 3',
	    	icon : '/img/business2.jpg',
	    	image : 'temp/homeslide/alltiles.jpg', 
	    	summery : 'Use the same user accounts and groups in the cloud that you already use on Use the same user accounts and groups in the cloud that you already use on premises. Use the same user accounts and groups in the cloud that you already use on premises.',			
	    },
	    {
	    	handle: 'Keyno4',
	    	title : 'Integrate with your local directory 4',
	    	icon : '/img/business2.jpg',
	    	image : 'temp/homeslide/alltiles.jpg', 
	    	summery : 'Use the same user accounts and groups in the cloud that you already use on Use the same user accounts and groups in the cloud that you already use on premises. Use the same user accounts and groups in the cloud that you already use on premises.',			
	    },
	    {
	    	handle: 'Keyno5',
	    	title : 'Integrate with your local directory 5',
	    	icon : '/img/business2.jpg',
	    	image : 'temp/homeslide/alltiles.jpg', 
	    	summery : 'Use the same user accounts and groups in the cloud that you already use on Use the same user accounts and groups in the cloud that you already use on premises. Use the same user accounts and groups in the cloud that you already use on premises.',			
	    }
	  ];	
});

/**
 * @ngdoc controller
 * @name RootCtrl
 *
 * @description
 * The root controller having a scope of the body element and methods used in the application wide
 * such as user authentications.
 *
 */
noteApp.controllers.controller('RootCtrl', function ($scope, $location,$anchorScroll) {

    /**
     * Returns if the viewLocation is the currently viewed page.
     *
     * @param viewLocation
     * @returns {boolean} true if viewLocation is the currently viewed page. Returns false otherwise.
     */
    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    }; 

    /**
     * Collapses the navbar on mobile devices.
     */
    $scope.collapseNavbar = function () {
        angular.element(document.querySelector('.navbar-collapse')).removeClass('in');
    };
    $scope.goToTop = function () {
    	window.scrollTo(0, 0);
    };

});