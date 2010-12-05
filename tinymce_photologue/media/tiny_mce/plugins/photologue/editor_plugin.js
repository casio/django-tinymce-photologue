(function() {
	tinymce.create('tinymce.plugins.PhotologuePlugin', {
		init : function(ed, url) {
			// Register commands
			ed.addCommand('mcePhotologueImage', function() {
				// Internal image object like a flash placeholder
				if (ed.dom.getAttrib(ed.selection.getNode(), 'class').indexOf('mceItem') != -1)
					return;

                var photologue_url = ed.dom.win.photologue_plugin_url;
				ed.windowManager.open({
					file : photologue_url,
					width : 520 + parseInt(ed.getLang('advimage.delta_width', 0)),
					height : 385 + parseInt(ed.getLang('advimage.delta_height', 0)),
					inline : 1
				}, {
					plugin_url : url
				});
			});

			// Register buttons
			ed.addButton('photologue', {
				title : 'photologue.image_desc',
				cmd : 'mcePhotologueImage',
                image : url + '/img/sample.gif'
			});
		},

		getInfo : function() {
			return {
				longname : 'Photologue',
                /*
				author : '',
				authorurl : '',
				infourl : '',
                */
				version : tinymce.majorVersion + "." + tinymce.minorVersion
			};
		}
	});

	// Register plugin
	tinymce.PluginManager.add('photologue', tinymce.plugins.PhotologuePlugin);
})();
